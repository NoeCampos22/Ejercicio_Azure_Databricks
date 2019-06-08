#-------------------------------------------------------------------------
# Script encargado de conectarse a un EventHub de Azure, para recibir los 
# tweet que se enviaron para su análisis de sentimiento: Obtener idioma,
# Score del sentimiento, Palabras claves y Entidades. Para finalmente
# guardar el objeto resultante en una table storage.
#
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install azure-eventhub"
#   4-. Ingresar el comando "pip install azure-storage"
#   5-. Ingresar el comando "pip install --upgrade azure-cognitiveservices-language-textanalytics"
#   6-. Tener el resto de archivos .py que se importan:
#           a) TextAnalytics
#           b) TableStorage
#           c) Credentials
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
#--------------------------------------------------------------------------

# Los imports generales
import json
import asyncio

# Se importan modulos de otros archivos .py
import Imports.Credentials as Credentials
from Imports.TextAnalytics import TextAnalytics
from Imports.TableStorage import TableStorage

# Importa lo necesario del Event Processor Host
from azure.eventprocessorhost import (
    AbstractEventProcessor,
    AzureStorageCheckpointLeaseManager,
    EventHubConfig,
    EventProcessorHost,
    EPHOptions)

# VARIABLES GLOBALES
# Conectar para trabajar con el storage
STG_Table = '-'
# Conectar al API de Text Analytics
TA_CogServices = '-'


# Clase para manejar la llegada de eventos, se encarga de abrir la conexión,
# cerrarla y procesar los eventos.
class EventProcessor(AbstractEventProcessor):

    # Constructor de un Event Processor
    def __init__(self, params=None):
        super().__init__(params)
        self._msg_counter = 0

    async def open_async(self, context):
        """
        Función que se puede hacer override
        Es para inicializar un Procesador de Eventos
        """
        print("Connection established {}".format(context.partition_id))

    
    
    async def close_async(self, context, reason):
        """
        Función que se puede hacer override
        Sirve para detener el Procesador de Eventos.
        """

        print("Connection closed (reason {}, id {}, offset {}, sq_number {})".format(
            reason,
            context.partition_id,
            context.offset,
            context.sequence_number))

    
    
    async def process_events_async(self, context, messages):
        """
            Función que se puede hacer override

            Se llama cuando el EPH recibe un nuevo batch de eventos.
            Es donde se programa las acciones a realizar.
            Parametros:
                context     = Información sobre la partición
                messages    = El batch de eventos a procesar
        """

        # Arreglo para guardar los tweets recibidos del Event Hub
        TA_Array = []

        # Se obtiene los JSON de todos los Tweets
        for Msg in messages:
            tempMsg = json.loads(Msg.body_as_str())
            TA_Array.append(tempMsg)

        # ================ Obtener los lenguajes ================ #

        # Se detecta los lenguajes
        LanguagesRes = TA_CogServices.detectLanguages(TA_Array)

        iI = 0  # Indice para moverse en el arreglo de tweets
        # Se agrega el lenguaje detectado a cada tweet
        for Doc in LanguagesRes.documents:
            TA_Array[iI]['language'] = Doc.detected_languages[0].iso6391_name
            iI += 1

        # ========== Realizar todos las operaciones ============ #

        # Se analiza el sentimiento
        ScoreRes = TA_CogServices.analyzeSentiment(TA_Array)
        # Se analiza las frases clave
        KeyPhrasesRes = TA_CogServices.keyPhrases(TA_Array)
        # Se obtiene las entidades
        EntitiesRes = TA_CogServices.identifyEntites(TA_Array)

        # =========== Obtener Score del Sentimiento ============ #

        iI = 0  # Indice para moverse en el arreglo de tweets
        # Se agrega el score del sentimiento al tweet
        for Doc in ScoreRes.documents:
            TA_Array[iI]['Sentiment_Score'] = float("{:.2f}".format(Doc.score))
            iI += 1

        # ================ Obtener Key Phrases ================= #

        iI = 0  # Indice para moverse en el arreglo de tweets
        # Juntan todas las key phrases en solo string y se agregan al tweet
        # al que corresponden
        for Doc in KeyPhrasesRes.documents:
            strKP = ""  # String temporal
            # Va por el arreglo de Key Phrases de ese tweet
            for Phrase in Doc.key_phrases:
                # Los junta
                strKP += Phrase + " | "

            # Agrega el atributo
            TA_Array[iI]['Key_Phrases'] = strKP
            iI += 1

        # ================== Obtener Entidades ================== #

        iI = 0  # Indice para moverse en el arreglo de tweets
        # Junta todas las entidades de cada Tweet
        for Doc in EntitiesRes.documents:
            strEnt = ""  # String temporal
            # Va por el arreglo de Entities de ese tweet
            for Entity in Doc.entities:
                # Junta las entidades
                strEnt += Entity.name + " | "

            # Agrega el atributo
            TA_Array[iI]['Entities'] = strEnt
            iI += 1

        # Se cambia la cambia el row de "id" a "Rowkey"
        STG_Array = json.loads(json.dumps(TA_Array).replace("\"id\":", "\"RowKey\":"))

        # =================== GUARDAR TWEETS =================== #
        # Por cada evento...
        for Tweet in STG_Array:
            # Se agrega a la tabla el tweet
            STG_Table.insertEntity("Tweets", Tweet)
            print(".")

        # Deja un checkpoint del evento recibido
        await context.checkpoint_async()



    async def process_error_async(self, context, error):
        # Función que se puede hacer override
        """
            Se llama cada que el cliente experimenta algún error al recibir eventos.
            El Event Proccessor Host se recupera recibiendo desde donde se quedo.
            ( A menos de que se haya matado el programa )
            Parametros:
                context     = Información sobre la partición
                messages    = El batch de eventos a procesar
        """
        print("Event Processor Error {!r}".format(error))



# Recibir eventos por dos minutos y luego apagarlo
async def wait_and_close(host):
    await asyncio.sleep(3600)
    await host.close_async()



# Se conecta y recibe mensajes
try:
    # Crea una instancia del objecto Table Storage
    STG_Table = TableStorage(Credentials.STG_ConnectionString)

    # Crea una Table service
    STG_Table.CreateTableServices()

    # Instancia del obketo Text Analytics
    TA_CogServices = TextAnalytics(
        Credentials.TA_SubsKey, Credentials.TA_Location)

    """
    Configuración del Event Hub
    Párametros:
        sb_name   = Nombre del namespace de Event Hubs
        eh_name   = Nombre del Event Hub
        policy    = Nombre del SAS Policy
        key       = Llave de la SAS Policy
    """
    EPH_Config = EventHubConfig(
        Credentials.EH_Namespace, Credentials.EH_Name, Credentials.EH_SASUser, Credentials.EH_SASKey)

    # Opciones por default
    EPH_Options = EPHOptions()
    # Set algunas opciones
    EPH_Options.release_pump_on_timeout = True
    EPH_Options.debug_trace = False

    """
    Configuración del Storage
    Párametros:
        lease_container_name    = Nombre del contenedor
        connection_string       = Link de conexión al storage account
    """
    STG_Manager = AzureStorageCheckpointLeaseManager(
        lease_container_name=Credentials.STG_BlobName, connection_string=Credentials.STG_ConnectionString)

    # while True:
    # Regresa un loop asincrono
    EPH_Loop = asyncio.get_event_loop()

    # Host del Event Hub Processor
    EPH_Host = EventProcessorHost(
        EventProcessor,
        EPH_Config,
        STG_Manager,
        ep_params=["param1", "param2"],
        eph_options=EPH_Options,
        loop=EPH_Loop)

    # Prepara los procedimientos a ejecutar en loop
    EPH_Tasks = asyncio.gather(
        EPH_Host.open_async(),
        wait_and_close(EPH_Host))

    # Corre el loop
    EPH_Loop.run_until_complete(EPH_Tasks)


# En caso de ocurrri excepciones de teclado
except KeyboardInterrupt:
    # Cancela las tareas y el loop
    for task in asyncio.Task.all_tasks():
        task.cancel()
    EPH_Loop.run_forever()
    EPH_Tasks.exception()

# Cierra el loop
finally:
    EPH_Loop.stop()

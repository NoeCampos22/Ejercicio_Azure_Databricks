#-------------------------------------------------------------------------
# Script en python que se encarga de conectarse a un recurso Event Hub de 
# Microsoft Azure y leer todos los mensajes disponibles, al mismo tiempo
# que deja un checkpoint de lo que ha leído para no repetir mensajes 
# la siguiente vez que arranque el programa.
#
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install azure-eventhub"
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
#--------------------------------------------------------------------------

import os
import sys
import json
import signal
import logging
import asyncio
import functools
from azure.eventprocessorhost import (
    AbstractEventProcessor,
    AzureStorageCheckpointLeaseManager,
    EventHubConfig,
    EventProcessorHost,
    EPHOptions)


class EventProcessor(AbstractEventProcessor):

    # Constructor de un Event Processor
    def __init__(self, params=None):
        super().__init__(params)
        self._msg_counter = 0

    # Función que se puede hacer override
    # Es para inicializar un Procesador de Eventos
    async def open_async(self, context):
        print("Connection established {}".format(context.partition_id))

    # Función que se puede hacer override
    # Sirve para detener el Procesador de Eventos.
    async def close_async(self, context, reason):

        print("Connection closed (reason {}, id {}, offset {}, sq_number {})".format(
            reason,
            context.partition_id,
            context.offset,
            context.sequence_number))

    # Función que se puede hacer override
    """
        Se llama cuando el EPH recibe un nuevo batch de eventos.
        Es donde se programa las acciones a realizar.
        Parametros:
            context     = Información sobre la partición
            messages    = El batch de eventos a procesar
    """
    async def process_events_async(self, context, messages):
        # Por cada evento...
        for Event in messages:
            # Se imprime el número de secuencia
            print("Mensaje: {}".format(Event.sequence_number))

            # Se parsea el json recibido en el mensaje del evento
            parsedMessage = json.loads(Event.body_as_str())
            # Se imprime de manera más estetica
            print(json.dumps(parsedMessage, indent=2, sort_keys=True))

        # Deja un checkpoint del evento recibido
        await context.checkpoint_async()

    # Función que se puede hacer override
    """
        Se llama cada que el cliente experimenta algún error al recibir eventos.
        El Event Proccessor Host se recupera recibiendo desde donde se quedo.
        ( A menos de que se haya matado el programa )
        Parametros:
            context     = Información sobre la partición
            messages    = El batch de eventos a procesar
    """
    async def process_error_async(self, context, error):
        print("Event Processor Error {!r}".format(error))

# Recibir eventos por dos minutos y luego apagarlo
async def wait_and_close(host):
    await asyncio.sleep(60)
    await host.close_async()

# Se conecta y recibe mensajes
try:
    # Regresa un loop asincrono
    ephLoop = asyncio.get_event_loop()

    # Nombre del Storage Account
    stgName = "-"
    # Key del storage
    stgKey = "-"
    # Nombre del Blob
    blobName = "-"

    # Nombre del namespace de Event Hubs
    ehNamespace = "-"
    # Nombre del Event Hub
    ehName = "-"
    # Nombre del SAS Policy del Event Hub
    SASUser = "-"
    # Llave del SAS Policy del Event Hub
    SASKey = "-"



    """
    Configuración del Event Hub
    Párametros:
        sb_name   = Nombre del namespace de Event Hubs
        eh_name   = Nombre del Event Hub
        policy    = Nombre del SAS Policy
        key       = Llave de la SAS Policy
    """
    ehConfig = EventHubConfig(ehNamespace, ehName, SASUser, SASKey)

    # Opciones por default
    ehOptions = EPHOptions()
    # Set algunas opciones
    ehOptions.release_pump_on_timeout = True
    ehOptions.debug_trace = False

    """
    Configuración del Storage
    Párametros:
        storage_account_name    = Nombre del storage
        storage_account_key     = Llave del storage
        lease_container_name    = Nombre del contenedor
    """
    stgManager = AzureStorageCheckpointLeaseManager(
        stgName, stgKey, blobName)

    # Host del Event Hub Processor
    ehHost = EventProcessorHost(
        EventProcessor,
        ehConfig,
        stgManager,
        ep_params = ["param1", "param2"],
        eph_options = ehOptions,
        loop = ephLoop)

    # Prepara los procedimientos a ejecutar en loop
    ephTasks = asyncio.gather(
        ehHost.open_async(),
        wait_and_close(ehHost))

    # Corre el loop
    ephLoop.run_until_complete(ephTasks)

# En caso de ocurrri excepciones de teclado
except KeyboardInterrupt:
    # Cancela las tareas y el loop
    for task in asyncio.Task.all_tasks():
        task.cancel()
    ephLoop.run_forever()
    ephTasks.exception()

# Cierra el loop
finally:
    ephLoop.stop()

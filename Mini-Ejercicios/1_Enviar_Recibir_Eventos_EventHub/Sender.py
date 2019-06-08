#-------------------------------------------------------------------------
# Programa que se encarga de conectarse con un recurso de Event Hub
# de Microsoft Azure y le envía N mensajes.
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
import time
import datetime
from azure.eventhub import EventHubClient, Sender, EventData

# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
ehAddress = "-"

# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
SASName = "_"
# Llave de acceso para esa SAS
PrimaryKey = "-"

# Intenta conectarse y mandar los eventos
try:
    # En caso de no tener un URL valido
    if not ehAddress:
        # Notifica el error y termina el programa
        raise ValueError("No EventHubs URL supplied.")

    """
    La clase EventHubClient define una conexión para enviar y recibir eventos
    Párametros:
        address     = El URL para conectarse al Event Hub
        username    = El nompre del SAS Policy
        password    = La contraseña del SAS Policy
        debug       = Si se quiere hacer debug de la conexión
    """
    ehClient = EventHubClient(ehAddress, SASName, PrimaryKey, debug=False)

    # Agrega un sender para enviar los eventos
    ehSender = ehClient.add_sender()

    """ 
    Abre las conecciones y corre los clientes Sender/Receiver
    En caso de iniciar con exito no regresa nada y en caso contrario
    va a mostrar una excepción
    """
    ehClient.run()

    # Ejecuta el envío y cacha los posibles errores
    try:
        iN = 100                 # Número de eventos a enviar
        iniTime = time.time()    # Tiempo en el que comenzó el programa

        # Loop para enviar iN eventos
        for iI in range(iN):
            # Crea el JSON String a enviar como eventos
            message = "{ \"PartitionKey\": \"" + "PK" + str(iI) + "\", \"RowKey\": \"" + "RK" + str(
                iI) + "\", \"Text\": \"" + "NAaaaaaah" + "\", \"Fecha\": \"" + "12-12-19" + "\" }"

            # Imprime el número del eventos enviado
            print("Sending message: {}".format(str(iI)))

            # Envía el eventos
            ehSender.send(EventData(str(message)))

    # Si hay un error en el envió
    except:
        # Lo notifica
        raise

    # Si todo acaba correcto
    finally:

        endTime = time.time()          # Obtiene el tiempo final
        ehClient.stop()                # Detiene el cliente
        runTime = endTime - iniTime    # Obtiene la duración

        # Imprime la duración
        print("Runtime: {} seconds".format(runTime))

# Si se presiona Ctrl + C detiene el programa
except KeyboardInterrupt:
    # Pero no muestra el la excepción en consola
    pass

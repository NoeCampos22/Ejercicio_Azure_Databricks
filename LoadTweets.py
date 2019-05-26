##############################################################
##  Script en python para mandar N mensajes a un Event Hub  ##
##############################################################

import os
import sys
import time
import logging
import datetime
from azure.eventhub import EventHubClient, Sender, EventData

# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
sAddress = "amqps://EHspacename.servicebus.windows.net/eh_tweets"

# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
SASName = "RootManageSharedAccessKey"
# Llave de acceso para esa SAS
PrimaryKey = "LAv6rhfBxUhwJrI5kFDvHW+GFj866RWEZj38yk2OT6o="

# Intenta conectarse y mandar los mensajes
try:
    # En caso de no tener un URL valido
    if not sAddress:
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
    ehClient = EventHubClient(sAddress, SASName, PrimaryKey, debug=False)

    # Agrega un sender para enviar los mensajes
    ehSender = ehClient.add_sender()

    """ 
    Abre las conecciones y corre los clientes Sender/Receiver
    En caso de iniciar con exito no regresa nada y en caso contrario
    va a mostrar una excepción
    """
    ehClient.run()

    # Ejecuta el envío y cacha los posibles errores
    try:
        iN = 100
        start_time = time.time()
        for i in range(iN):
            message = "{ \"PartitionKey\": \"" + "PK" + str(i) + "\", \"RowKey\": \"" + "RK" + str(
                i) + "\", \"Tweet\": \"" + "NAaaaaaah" + "\", \"Fecha\": \"" + "12-12-19" + "\" }"
            print("Sending message: {}".format(message))
            ehSender.send(EventData(str(message)))
    except:
        raise
    finally:
        end_time = time.time()
        ehClient.stop()
        run_time = end_time - start_time
        print("Runtime: {} seconds".format(run_time))

except KeyboardInterrupt:
    pass

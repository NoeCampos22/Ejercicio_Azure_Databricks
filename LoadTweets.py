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
        iN = 100                    # Número de mensajes a enviar
        start_time = time.time()    # Tiempo en el que comenzó el programa

        # Loop para enviar iN mensajes
        for iI in range(iN):
            # Crea el JSON String a enviar como mensaje
            message = "{ \"PartitionKey\": \"" + "PK" + str(iI) + "\", \"RowKey\": \"" + "RK" + str(
                iI) + "\", \"Tweet\": \"" + "NAaaaaaah" + "\", \"Fecha\": \"" + "12-12-19" + "\" }"

            # Imprime el número del mensaje enviado
            print("Sending message: {}".format(str(iI)))

            # Envía el mensaje
            ehSender.send(EventData(str(message)))

    # Si hay un error en el envió
    except:
        # Lo notifica
        raise

    # Si todo acaba correcto
    finally:

        end_time = time.time()              # Obtiene el tiempo final
        ehClient.stop()                     # Detiene el cliente
        run_time = end_time - start_time    # Obtiene la duración

        # Imprime la duración
        print("Runtime: {} seconds".format(run_time))

# Si se presiona Ctrl + C detiene el programa
except KeyboardInterrupt:
    # Pero no muestra el la excepción en consola
    pass

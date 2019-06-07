#--------------------------------------------------------------------------
#   Script en python para recibir TODOS los eventos de un Event Hub   
#   pero solo utiliza una partición.                                  
#--------------------------------------------------------------------------

import os
import sys
import time
import logging
from azure.eventhub import EventHubClient, Receiver, Offset

# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
ehAddress = "amqps://EHTweets.servicebus.windows.net/eh_tweets"

# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
SASName = "RootManageSharedAccessKey"
# Llave de acceso para esa SAS
PrimaryKey = "XGpR/C3HHTdKN9NcrSD7nHHbpRglgk0VUmc1hhFlybs="

# Nombre del grupo consumidor
ConsumerGruop = "$default"
# Offset desde el que se quiere empezar a recibir eventos
OFFSET = Offset("-1")
# ID de la partición a utilizar del Event Hub
Partition = "0"

iTotal = 0         # Total de eventos recibidos
lastSN = -1        # Last sequence number
lasOffset = "-1"   # Received offset

"""
La clase EventHubClient define una conexión para enviar y recibir eventos
Párametros:
    address     = El URL para conectarse al Event Hub
    username    = El nompre del SAS Policy
    password    = La contraseña del SAS Policy
    debug       = Si se quiere hacer debug de la conexión
"""
ehClient = EventHubClient(sAddress, SASName, PrimaryKey, debug=False)

# Se conecta y recibe los eventos o atrapa cualquier posible error
try:
    """
    Crea un objeto Receiver.
    Parametros: 
        consumer_group      = Nombre del grupo consumidor
        partition           = ID de la partición
    """
    receiver = ehClient.add_receiver(ConsumerGruop, Partition)

    # Arranca el cliente
    ehClient.run()
    # Obtiene el tiempo inicial
    start_time = time.time()

    # Obtiene el primer batch de eventos
    evBatch = receiver.receive(timeout=1000)

    # Mientras que la variable bach contenga eventos
    while evBatch:

        # Por cada evento...
        for Event in evBatch:

            lasOffset = Event.offset         # Obtener el offset del mensaje
            lastSN = Event.sequence_number   # Se obtiene el número de secuencia

            # Se imprime el offset del mensaje 
            print("Received: {}, {}".format(lasOffset.value, lastSN))
            # Se imprime el contenido del mensaje
            print(Event.body_as_str())
            # Se aumenta en uno el total de mensajes recibidos
            iTotal += 1
            # Obtiene el tiempo en que termino de procesar el evento
            end_time = time.time()

        # Obtiene el siguiente batch de eventos
        # en caso de que en 10 segundos no encuentre nada el loop termina
        evBatch = receiver.receive(timeout = 10)
    
    # Detiene el cliente para dejar de recibir eventos
    ehClient.stop()
    # Calcula el tiempo que estuvo recibiendo eventos
    run_time = end_time - start_time

    # Imprime el resultado final
    print("Received {} messages in {} seconds".format(iTotal, run_time))

# Si hay una excepción del teclado, detiene el programa pero
# no lo muestra en consola.
except KeyboardInterrupt:
    pass
# Y detiene al cliente
finally:
    ehClient.stop()

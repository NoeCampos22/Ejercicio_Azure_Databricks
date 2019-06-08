#-------------------------------------------------------------------------
# Script para conectarse a un Event Hub y recibir los mensajes, pero
# son TODOS los que estan disponibles en el Event Hub
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
import logging
from azure.eventhub import EventHubClient, Receiver, Offset

# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
EH_Address = "-"

# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
EH_SASName = "-"
# Llave de acceso para esa SAS
EH_PrimaryKey = "-"

# Nombre del grupo consumidor
EH_ConsumerGruop = "-"
# Offset desde el que se quiere empezar a recibir eventos
OFFSET = Offset("-1")
# ID de la partición a utilizar del Event Hub
EH_Partition = "0"

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
EH_Client = EventHubClient(EH_Address, EH_SASName, EH_PrimaryKey, debug=False)

# Se conecta y recibe los eventos o atrapa cualquier posible error
try:
    """
    Crea un objeto Receiver.
    Parametros: 
        consumer_group      = Nombre del grupo consumidor
        partition           = ID de la partición
    """
    EH_Receiver = EH_Client.add_receiver(EH_ConsumerGruop, EH_Partition)

    # Arranca el cliente
    EH_Client.run()
    # Obtiene el tiempo inicial
    start_time = time.time()

    # Obtiene el primer batch de eventos
    evBatch = EH_Receiver.receive(timeout=1000)

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
        evBatch = EH_Receiver.receive(timeout = 10)
    
    # Detiene el cliente para dejar de recibir eventos
    EH_Client.stop()
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
    EH_Client.stop()

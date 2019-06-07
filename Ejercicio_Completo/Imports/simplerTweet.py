#-------------------------------------------------------------------------
# Clase para crear una conexión y poder hacer uso 
# del funciones en un Storage Account, especificamente para Table Storage.
#  
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install azure-storage"
#
# Autor: Noé Amador Campos Castillo.
# E-mail: ama-noe@hotmail.com
#--------------------------------------------------------------------------

import re
import datetime

class simplerTweet:
    """
    Es una clase para solo guardar el ID y Texto, apatir de un objeto 
    Tweet origianl de Twitter
    """
    # Constructor
    def __init__(self, ogTweet):
        self.PartitionKey = "Tweets"
        self.id = ogTweet['id_str']
        self.text = ogTweet['text']

    # Para regresar el json
    def serialize(self):
        return self.__dict__


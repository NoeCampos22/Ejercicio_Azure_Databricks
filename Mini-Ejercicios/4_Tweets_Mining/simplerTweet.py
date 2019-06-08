#-------------------------------------------------------------------------
# Clase para simplificar el objeto Tweet Original.
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
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

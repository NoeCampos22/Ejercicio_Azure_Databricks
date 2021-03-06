#-------------------------------------------------------------------------
# Script encargada de conectarse a la API Tweepy, para escuchar
# y traerse los tweets que cumplan con el filtro especificado.
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
#--------------------------------------------------------------------------

# Se importa Tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

# Importar la clase Tweet del proyecto
from simplerTweet import simplerTweet

# Importa las credenciales para el proyecto
import Tw_Credentials

# Otros imports necesarios
import json
import time
import pprint

def Get_Authentication():
    """
    Para validar con Twitter las credenciales de la Twitter App
    """
    Auth = OAuthHandler(Tw_Credentials.CON_KEY,
                        Tw_Credentials.CON_KEY_SECRET)
    # Valida los tokens de acceso
    Auth.set_access_token(Tw_Credentials.ACC_TOKEN,
                            Tw_Credentials.ACC_TOKEN_SECRET)
    return Auth


class MyStreamListener(StreamListener):

    # Revisa si hubo un error al escuchar twits
    def on_error(self, status):
        # status 420 es para detener el proceso
        if status == 420:
            return False
        # Imprimir el error
        print(status)

    def on_data(self, data):
        """
        Aquí se define que se va hacer cuando se reciba datos
        """
        try:
            # Cambia el formato de caracteres
            encoded = data.encode('utf-8')
            # Carga el objeto Tweet que regresa la API
            parsed = json.loads(encoded)

            # Crea un objeto Tweet filtrado
            filterTweet = simplerTweet(parsed).serialize()

            # Crea un objeto Pretty Printer para el json
            pp = pprint.PrettyPrinter(indent = 4)

            # Imprime el JSON
            pp.pprint(filterTweet)
            print()

            return True

        # Si hay un error, lo cacha
        except BaseException as e:
            # Y lo imprime
            print("->Error on data: %s" % str(e))

        return True


if __name__ == '__main__':
    # Un arreglo con las palabras claves a buscar
    keyPhrases = ['#AvengersEndGame, EndGame, #Avengers, Avengers, #Vengadores, #LiguillaMX, @GameOfThrones, #ForTheThrone, #GameofThrones, @Marvel, @Avengers, @Wendy']

    print("====== Running App ======")
    try:

        # Obtiene la autenticación de las credenciales
        Auth = Get_Authentication()
        # Crea el objeto listener de tweets
        myStreamListener = MyStreamListener()
        # Crea el objeto para empezar a recibir tweets
        myStream = Stream(Auth, myStreamListener)

        print(">> Listening tweets")

        # Filtra tweets por las palabras clave
        myStream.filter(track=keyPhrases,  stall_warnings=True)

    # Si se presion Ctrl + C, termina el programa
    except KeyboardInterrupt:
        print()
        pass

    # Cacha algun error que ocurra
    except Exception as err:
        # Lo imprime
        print(err)

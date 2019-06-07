#-------------------------------------------------------------------------
# Script encargado de conectarse a una aplicación de Twitter, utilizando
# la API Tweepy para escuchar y obtener los tweets que pasen por el filtro
# establecido previamente. Una vez que se obtiene un tweet se manda a un
# recurso Event Hub en Azure.
#
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install azure-eventhub"
#   4-. Ingresar el comando "pip install tweepy"
#   6-. Tener el resto de archivos .py que se importan:
#           a) simplerTweet
#           b) Credentials
#
# Autor: Noé Amador Campos Castillo.
# E-mail: ama-noe@hotmail.com
#--------------------------------------------------------------------------

# Imports generales
import json
import time

# Importar la clase Tweet del proyecto
from Imports.simplerTweet import simplerTweet

# Importa las credenciales para el proyecto
import Imports.Credentials as Credentials

# Se importa la API de Tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

# Se importa lo necesario para usar el Event Hub Client
from azure.eventhub import EventHubClient, Sender, EventData

# VARIABLES GENERALES
# Conexión al Event Hub
EH_Sender = '-'


def Get_Authentication():
    """
    Para validar con Twitter las credenciales de la Twitter App
    """
    Auth = OAuthHandler(Credentials.CON_KEY, Credentials.CON_KEY_SECRET)
    # Valida los tokens de acceso
    Auth.set_access_token(Credentials.ACC_TOKEN, Credentials.ACC_TOKEN_SECRET)
    return Auth


# Clase para crear un listener de tweets
class MyStreamListener(StreamListener):

    def on_error(self, status):
        """
        Revisa si hubo un error al escuchar tweets
        """
        # status 420 es para detener el proceso
        if status == 420:
            return False
        # Imprimir el error
        print(status)

    def on_data(self, data):
        """
        Aquí se define que se va hacer cuando el programa 
        reciba un tweet
        """
        try:
            # Cambia el formato de caracteres
            Tw_encoded = data.encode('utf-8')
            # Carga el objeto Tweet que regresa la API
            Tw_parsed = json.loads(Tw_encoded)

            # Crea un objeto Tweet simplificado
            sTweet = simplerTweet(Tw_parsed).serialize()

            # Obtiene el json del tweet
            strTweet = json.dumps(sTweet, ensure_ascii=False)

            # Envía el json
            EH_Sender.send(EventData(strTweet))

            # Imprime JSON
            print(strTweet)
            print()

            return True

        # En caso de que se presione Ctrl + C
        except KeyboardInterrupt:
            # Imprime un espacio
            print()
            pass

        # Si hay un error, lo cacha
        except BaseException as e:
            # Y lo imprime
            print("->Error on data: %s" % str(e))

        return True


if __name__ == '__main__':
    # Un arreglo con las palabras claves a buscar
    KeyPhrases = [
        '#AvengersEndGame, EndGame, #Avengers, Avengers, #Vengadores, @GameOfThrones, #ForTheThrone, #GameofThrones, @Marvel, @Avengers, @Wendy']
    # KeyPhrases = ['@TecdeMonterrey', '#OrgulloTec', '#EXATEC', '#SomosTec']

    print("====== Running App ======")
    try:

        # La clase EventHubClient define una conexión para enviar y recibir eventos
        EH_Client = EventHubClient(
            Credentials.EH_Address, Credentials.EH_SASName, Credentials.EH_PrimaryKey, debug=False)
        # Agrega un sender para enviar los eventos
        EH_Sender = EH_Client.add_sender()
        # Abre las conecciones y corre los clientes Sender/Receiver
        EH_Client.run()

        # Obtiene la autenticación de las credenciales
        Auth = Get_Authentication()
        # Crea el objeto listener de tweets
        myStreamListener = MyStreamListener()
        # Crea el objeto para empezar a recibir tweets
        myStream = Stream(Auth, myStreamListener)

        print(">> Listening tweets")

        # Filtra tweets por las palabras clave
        myStream.filter(track=KeyPhrases,  stall_warnings=True)

    # Si se presion Ctrl + C, termina el programa
    except KeyboardInterrupt:
        EH_Client.stop()
        pass

    # Cacha algun error que ocurra
    except Exception as err:
        # Lo imprime
        print(err)

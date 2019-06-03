# Se importa Tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from azure.eventhub import EventHubClient, Sender, EventData

# Importar la clase Tweet del proyecto
from filteredTweet import filteredTweet

# Importa las credenciales para el proyecto
import Credentials

# Otros imports necesarios
import json
import time
import pprint

ehSender = '-'

def Get_Authentication():
    """
    Para validar con Twitter las credenciales de la Twitter App
    """
    Auth = OAuthHandler(Credentials.CON_KEY, Credentials.CON_KEY_SECRET)
    # Valida los tokens de acceso
    Auth.set_access_token(Credentials.ACC_TOKEN, Credentials.ACC_TOKEN_SECRET)
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
            fTweet = filteredTweet(parsed).serialize()
            
            # Obtiene el json del tweet
            strTweet = json.dumps(fTweet, ensure_ascii=False)
            
            # Lo envía
            ehSender.send(EventData(strTweet))

            # Imprime JSON
            print(strTweet)
            print()

            return True

        except KeyboardInterrupt:
            print()
            pass

        # Si hay un error, lo cacha
        except BaseException as e:
            # Y lo imprime
            print("->Error on data: %s" % str(e))

        return True


if __name__ == '__main__':
    # Un arreglo con las palabras claves a buscar
    keyPhrases = ['#AvengersEndGame, EndGame, #Avengers, Avengers, #Vengadores, @GameOfThrones, #ForTheThrone, #GameofThrones, @Marvel, @Avengers, @Wendy']
    # keyPhrases = ['@TecdeMonterrey', '#OrgulloTec', '#EXATEC', '#SomosTec']

    print("====== Running App ======")
    try:

        #La clase EventHubClient define una conexión para enviar y recibir eventos
        ehClient = EventHubClient(Credentials.EH_Address, Credentials.EH_SASName, Credentials.EH_PrimaryKey, debug=False)
        # Agrega un sender para enviar los eventos
        ehSender = ehClient.add_sender()
        #Abre las conecciones y corre los clientes Sender/Receiver
        ehClient.run()

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
        ehClient.stop()
        pass

    # Cacha algun error que ocurra
    except Exception as err:
        # Lo imprime
        print(err)

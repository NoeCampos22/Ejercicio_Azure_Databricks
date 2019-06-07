#-------------------------------------------------------------------------
# Es una clase escrita en Python para facilitar el uso de los objetos y
# herramientas de Cognitive Services de Mircrosoft Azure.
# Se inicializa dando la llave de subscripción y la locación del recurso.
# Sirve para:
#   1- Detectar el lenguaje
#   2- Analizar el sentimiento
#   3- Obtener las palabras claves
#   4- Obtener las entidades
#
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   2-. Ingresar el comando "pip install --upgrade azure-cognitiveservices-language-textanalytics"
#
# Autor: Noé Amador Campos Castillo.
# E-mail: ama-noe@hotmail.com
#--------------------------------------------------------------------------

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

class TextAnalytics():

    """
    Constructor: Se encarga de validar las credenciales y hacer la conexión
    con el recurso en Azure.

    Parametros:
        SubscriptionKey     = La llave perteneciente al recurso de Cognitive Services
        Location            = La locación del recurso, por ejemplo "eastus" o "westus"
    """

    def __init__(self, SubscriptionKey, Location):
        SubscriptionKey = SubscriptionKey
        TA_URL = "https://{0}.api.cognitive.microsoft.com/".format(Location)

        Credentials = CognitiveServicesCredentials(SubscriptionKey)

        self.Text_Analytics = TextAnalyticsClient(
            endpoint=TA_URL, credentials=Credentials)

    def detectLanguages(self, Documents):
        """
        Función encargada de hacer el llamado para detectar el lenguaje
        y regresar el arreglo de lenguajes.

        Parametros:
            Documents   =   El arreglo con los objetos a analizar. Estos objetos DEBEN de tener
                            los atributos "id" y "text".
        """
        arrLanguages = self.Text_Analytics.detect_language(documents=Documents)

        return arrLanguages

    def analyzeSentiment(self, Documents):
        """
        Función encargada de hacer el llamado para analizar el sentimiento y obtener un arreglo
        con los puntjaes.

        Parametros:
            Documents   =   El arreglo con los objetos a analizar. Estos objetos DEBEN de tener
                            los atributos "id", "langugae" y "text".
        """
        arrScore = self.Text_Analytics.sentiment(documents=Documents)

        return arrScore

    def keyPhrases(self, Documents):
        """
        Función encargada de hacer el llamado para obtener un arreglo con las palabras clave

        Parametros:
            Documents   =   El arreglo con los objetos a analizar. Estos objetos DEBEN de tener
                            los atributos "id", "langugae" y "text".
        """
        matKeyPhrases = self.Text_Analytics.key_phrases(documents=Documents)

        return matKeyPhrases

    def identifyEntites(self, Documents):
        """
        Función encargada de hacer el llamado para identificar las entidades
        Parametros:
            Documents   =   El arreglo con los objetos a analizar. Estos objetos DEBEN de tener
                            los atributos "id" y "text".
        """
        matEntitites = self.Text_Analytics.entities(documents=Documents)

        return matEntitites

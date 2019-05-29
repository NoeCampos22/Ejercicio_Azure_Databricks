from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

class TextAnalytics():

    def __init__(self, SubscriptionKey, Location):
        self.SubscriptionKey = SubscriptionKey
        self. TA_URL = "https://{0}.api.cognitive.microsoft.com/".format(Location)

        self.Credentials = CognitiveServicesCredentials(SubscriptionKey)

        self.Text_Analytics = TextAnalyticsClient(endpoint = self.TA_URL
        , credentials = self.Credentials)

    
    def detectLanguages(self, Documents):
        arrLanguages = self.Text_Analytics.detect_language(documents = Documents)

        return arrLanguages

    def analyzeSentiment(self, Documents):
        arrScore = self.Text_Analytics.sentiment(documents = Documents)

        return arrScore

    def keyPhrases(self, Documents):
        matKeyPhrases = self.Text_Analytics.key_phrases(documents = Documents)

        return matKeyPhrases

    def identifyEntites(self, Documents):
        matEntitites = self.Text_Analytics.entities(documents = Documents)
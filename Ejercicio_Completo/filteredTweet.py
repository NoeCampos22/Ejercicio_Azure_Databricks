import re
import datetime
import TextAnalytics

# It is a tweet class but only with the attributes that interest me
class filteredTweet:

    # Constructor
    def __init__(self, ogTweet):
        self.PartitionKey = "Tweets"
        self.id = ogTweet['id_str']
        self.text = ogTweet['text']
        
    # Private function to get the source
    def __getSource(self, ogTweet):
        cleanr = re.compile('<.*?>')
        self.source = re.sub(cleanr, '', ogTweet["source"])

    def serialize(self):
        return self.__dict__

        # self.language = '-'
        # self.SentimentScore = 0
        # self.KeyPhrases = ''
        # self.Entities = ''


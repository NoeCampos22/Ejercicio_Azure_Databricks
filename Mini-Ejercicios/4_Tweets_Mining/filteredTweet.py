import re
import datetime

# It is a tweet class but only with the attributes that interest me
class filteredTweet:

    # Constructor
    def __init__(self, ogTweet):
        self.lang = ogTweet['lang']
        self.text = ogTweet['text']
        self.__getSource(ogTweet)

    # Private function to get the source
    def __getSource(self, ogTweet):
        cleanr = re.compile('<.*?>')
        self.source = re.sub(cleanr, '', ogTweet["source"])

    def serialize(self):
        return self.__dict__

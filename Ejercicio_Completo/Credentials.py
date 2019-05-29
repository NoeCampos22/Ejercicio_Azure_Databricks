#========================== Twitter App ==========================#
# Variables con las llaves de acceso a la aplicación de Twitter
ACC_TOKEN = "1102066975541469184-TbS4fYGEvmq0Jltl91vs6E1dvVCqNO"
ACC_TOKEN_SECRET = "RCX08QzpIrnG2DmjEs8wTje0QDS9FdVsFTto1KW1M98b5"
CON_KEY = "o15XnHDzDvGWv3l1enwV58yBq"
CON_KEY_SECRET = "jON1UNSzhfk4eu5sws7RgLhpNCbkWsu06sRvwrKFjXwfu7uFHG"


#========================== Event Hub ==========================#
# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
ehAddress = "amqps://EHTweets.servicebus.windows.net/eh_tweets"

# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
ehSASName = "RootManageSharedAccessKey"
# Llave de acceso para esa SAS
ehPrimaryKey = "XGpR/C3HHTdKN9NcrSD7nHHbpRglgk0VUmc1hhFlybs="

#=========================== Storage ===========================#
# El string de conexión al storage account
stgConnectionString = 'DefaultEndpointsProtocol=https;AccountName=stgeducon;AccountKey=ZSiqHjaX+3yooxOVZbffjbjaKnlMHWyYHBtxH2ANxle3EDMSqZ66cd75HUT0Tr48QPYRJus7XkwPT6aJ2wrAyQ==;EndpointSuffix=core.windows.net'

#===================== Cognitive Services ======================#
TA_SubsKey = "8c5fb6709dc0410384e8fdb8da42a76f"
TA_Location = "eastus"

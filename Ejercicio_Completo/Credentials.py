#========================== Twitter App ==========================#
# Variables con las llaves de acceso a la aplicación de Twitter
ACC_TOKEN = "1102066975541469184-TbS4fYGEvmq0Jltl91vs6E1dvVCqNO"
ACC_TOKEN_SECRET = "RCX08QzpIrnG2DmjEs8wTje0QDS9FdVsFTto1KW1M98b5"
CON_KEY = "o15XnHDzDvGWv3l1enwV58yBq"
CON_KEY_SECRET = "jON1UNSzhfk4eu5sws7RgLhpNCbkWsu06sRvwrKFjXwfu7uFHG"

#========================== Event Hub ==========================#
# Nombre del namespace de Event Hubs
EH_Namespace = "EHTweets"
# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
EH_Address = "amqps://EHTweets.servicebus.windows.net/eh_tweets"
# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
EH_SASName = "RootManageSharedAccessKey"
# Llave de acceso para esa SAS
EH_PrimaryKey = "XGpR/C3HHTdKN9NcrSD7nHHbpRglgk0VUmc1hhFlybs="

# Nombre de la instancia del Event Hub
EH_Name = "eh_tweets"
# Nombre del SAS Policy de la instancia de Event Hub
EH_SASUser = "TweetsReceiver"
# Llave del SAS Policy de la instancia de Event Hub
EH_SASKey = "X6hcZGVDQmR7uFrwH5SuYNfHLiQxLiB+XMxky3BGwjA="

#=========================== Storage ===========================#
# El string de conexión al storage account
STG_ConnectionString = 'DefaultEndpointsProtocol=https;AccountName=stgeducon;AccountKey=ZSiqHjaX+3yooxOVZbffjbjaKnlMHWyYHBtxH2ANxle3EDMSqZ66cd75HUT0Tr48QPYRJus7XkwPT6aJ2wrAyQ==;EndpointSuffix=core.windows.net'
# Nombre del Blob
STG_BlobName = "contenedor"

#===================== Cognitive Services ======================#
TA_SubsKey = "8c5fb6709dc0410384e8fdb8da42a76f"
TA_Location = "eastus"

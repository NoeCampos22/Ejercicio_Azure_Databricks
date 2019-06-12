#-------------------------------------------------------------------------
# Script con las llaves, nombres y permisos necesarios para completar el
# ejercicio de analizar tweets utlizando una aplicación de Twitter,
# Event Hub de Azure, Cognitive Services y Table Storage-
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
#--------------------------------------------------------------------------

#========================== Twitter App ==========================#
# Variables con las llaves de acceso a la aplicación de Twitter
ACC_TOKEN = "1102066975541469184-TbS4fYGEvmq0Jltl91vs6E1dvVCqNO"
ACC_TOKEN_SECRET = "RCX08QzpIrnG2DmjEs8wTje0QDS9FdVsFTto1KW1M98b5"
CON_KEY = "o15XnHDzDvGWv3l1enwV58yBq"
CON_KEY_SECRET = "jON1UNSzhfk4eu5sws7RgLhpNCbkWsu06sRvwrKFjXwfu7uFHG"

#========================== Event Hub ==========================#
# Nombre del namespace de Event Hubs
EH_Namespace = "ehTweetsNamespace"
# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
EH_Address = "amqps://ehTweetsNamespace.servicebus.windows.net/eh_tweets"
# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
EH_SASName = "RootManageSharedAccessKey"
# Llave de acceso para esa SAS
EH_PrimaryKey = "/knjLPLvztPMXwAua62yiebka1BQptmCJhi7MhUPmi0="

# Nombre de la instancia del Event Hub
EH_Name = "eh_tweets"
# Nombre del SAS Policy de la instancia de Event Hub
EH_SASUser = "TweetsListener"
# Llave del SAS Policy de la instancia de Event Hub
EH_SASKey = "PgOMsgAvtRrmHV3gkS6H5W0F6w5xbwlqMPqvORpMq7Y="

#=========================== Storage ===========================#
# El string de conexión al storage account
STG_ConnectionString = 'DefaultEndpointsProtocol=https;AccountName=stgeducon;AccountKey=uIFr2p05ZeXU8XRBkpgG05eKINZkcxQncyWQOkOxUFKo2AV2fXONkZIGr3YTaFkV6aOGd6qybod/LjFRxtI2Xg==;EndpointSuffix=core.windows.net'
# Nombre del Blob
STG_BlobName = "contenedor"
# Nombre de tabla
STG_TableName = "Tweets"

#===================== Cognitive Services ======================#
TA_SubsKey = "456e4299826344658c4e0f4cbd815d10"
TA_Location = "eastus"

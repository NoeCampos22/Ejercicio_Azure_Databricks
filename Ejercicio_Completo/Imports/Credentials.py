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
ACC_TOKEN = "-"
ACC_TOKEN_SECRET = "-"
CON_KEY = "-"
CON_KEY_SECRET = "-"

#========================== Event Hub ==========================#
# Nombre del namespace de Event Hubs
EH_Namespace = "-"
# Dirección URL para conectarse al Event Hub
# "amqps://<Nombre del Event Hub Namespace>.servicebus.windows.net/<Nombre del Event Hub>"
EH_Address = "-"
# Nombre del "Shared Access Policy" configurado en el Event Hub Namespace
EH_SASName = "-"
# Llave de acceso para esa SAS
EH_PrimaryKey = "-"

# Nombre de la instancia del Event Hub
EH_Name = "-"
# Nombre del SAS Policy de la instancia de Event Hub
EH_SASUser = "-"
# Llave del SAS Policy de la instancia de Event Hub
EH_SASKey = "-"

#=========================== Storage ===========================#
# El string de conexión al storage account
STG_ConnectionString = '-'
# Nombre del Blob
STG_BlobName = "-"
# Nombre de tabla
STG_TableName = "_"

#===================== Cognitive Services ======================#
TA_SubsKey = "-"
TA_Location = "-"

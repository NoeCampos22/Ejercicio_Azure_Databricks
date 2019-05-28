#--------------------------------------------------------------------------
# Script en python hecho con fines de mostrar como se hace uso del REST API de 
# Text Analytics de Azure.
#
# Se hizo uso de la documentación en de Azure en python de Microsoft:
# https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python
#--------------------------------------------------------------------------

import requests
import json
from IPython.display import HTML

# La llave de recurso de Cognitive Services
subscription_key = "8c5fb6709dc0410384e8fdb8da42a76f"

# Es el link del recurso, el template es:
# "https://<location>.api.cognitive.microsoft.com/text/analytics/v2.1/"
text_analytics_base_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/"

# Son los links para las diferentes peticiones
language_api_url = text_analytics_base_url + "languages"
sentiment_url = text_analytics_base_url + "sentiment"
keyphrase_url = text_analytics_base_url + "keyPhrases"
entities_url = text_analytics_base_url + "entities"

# El header para el request
headers = {"Ocp-Apim-Subscription-Key": subscription_key}


################################# DETECT LANGUAGES #################################

"""
NOTA: Los datos se DEBEN MANDAR en un JSON con un atributo tipo arreglo llamado "documents"
y cada objecto del arreglo DEBE TENER el atributo "id" y el "text"  
"""

# Datos dummy
documents = {"documents": [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"}
]}

# Se hace el request al REST API
response = requests.post(language_api_url, headers = headers, json = documents)
# Se hace string el arreglo que regresa
languages = response.json()
# Se imprime el resultado
print("======= Detect languages ======")
print(json.dumps(languages, indent=2, sort_keys=True))
print("===============================\n\n")


################################# ANALYZE SENTIMIENT #################################

"""
NOTA: Los datos se DEBEN MANDAR en un JSON con un atributo tipo arreglo llamado "documents"
y cada objecto del arreglo DEBE TENER los atributos "id", "text" y "language"
"""

# Datos dummy
documents = {"documents": [
    {"id": "1", "language": "en",
        "text": "I had a wonderful experience! The rooms were wonderful and the staff was helpful."},
    {"id": "2", "language": "en",
        "text": "I had a terrible time at the hotel. The staff was rude and the food was awful."},
    {"id": "3", "language": "es",
        "text": "Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos."},
    {"id": "4", "language": "es",
     "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."}
]}

# Request al REST API
response = requests.post(sentiment_url, headers = headers, json = documents)
# Se obtiene el json 
sentiments = response.json()
# Se imprime 
print("====== Analyze sentiment ======")
print(json.dumps(sentiments, indent=2, sort_keys=True))
print("===============================\n\n")


################################# EXTRACT KEY PHRASES #################################

"""
NOTA: Los datos se DEBEN MANDAR en un JSON con un atributo tipo arreglo llamado "documents"
y cada objecto del arreglo DEBE TENER los atributos "id", "text" y "language"
"""

# Request al REST API
response = requests.post(keyphrase_url, headers = headers, json = documents)
# Se obtiene el json
key_phrases = response.json()
# Se imprime 
print("====== Extract Key Phrases ======")
print(json.dumps(key_phrases, indent=2, sort_keys=True))
print("=================================\n\n")


################################# IDENTIFY ENTITES #################################
"""
NOTA: Los datos se DEBEN MANDAR en un JSON con un atributo tipo arreglo llamado "documents"
y cada objecto del arreglo DEBE TENER los atributos "id", "text".
"""

# Dato dummy
documents = {"documents": [
    {"id": "1", "languages": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800."}
]}

response = requests.post(entities_url, headers = headers, json = documents)
entities = response.json()
print("======= Identify Entities =======")
print(json.dumps(entities, indent=2, sort_keys=True))
print("=================================\n\n")






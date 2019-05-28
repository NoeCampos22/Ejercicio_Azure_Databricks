#--------------------------------------------------------------------------
# Script en python hecho con fines de mostrar como se hace uso del REST API de
# Text Analytics de Azure.
#
# Se hizo uso de la documentación en de Azure en python de Microsoft:
# https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python-sdk
#--------------------------------------------------------------------------

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

# Llave del recurso de Cognitive services en Azure
subscription_key = "8c5fb6709dc0410384e8fdb8da42a76f"
# Objeto credenciales de cognitive services
credentials = CognitiveServicesCredentials(subscription_key)

# URL para conectarse al recurso, el template es:
# https://<location>.api.cognitive.microsoft.com/
text_analytics_url = "https://eastus.api.cognitive.microsoft.com/"

# Cliente de servicios de cognitivos
text_analytics = TextAnalyticsClient(
    endpoint = text_analytics_url, credentials = credentials)

################################# DETECT LANGUAGES #################################

# Datos dummy
documents = [
    {
        'id': '1',
        'text': 'This is a document written in English.'
    },
    {
        'id': '2',
        'text': 'Este es un documento escrito en Español.'
    },
    {
        'id': '3',
        'text': '这是一个用中文写的文件'
    }
]

# Se llama a la función para detectar el lenguaje
response = text_analytics.detect_language(documents = documents)

print("======= Detect languages ======")
# Como regresa un arreglo, hay que recorrerlo
for document in response.documents:
    # Se imprime el resultado de cada documento
    print("Document Id: ", document.id, ", Language: ",
          document.detected_languages[0].name)
print("===============================\n\n")


################################# ANALYZE SENTIMIENT #################################

# Datos dummy
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "I had the best day of my life."
    },
    {
        "id": "2",
        "language": "en",
        "text": "This was a waste of my time. The speaker put me to sleep."
    },
    {
        "id": "3",
        "language": "es",
        "text": "No tengo dinero ni nada que dar..."
    },
    {
        "id": "4",
        "language": "it",
        "text": "L'hotel veneziano era meraviglioso. È un bellissimo pezzo di architettura."
    }
]

# Se llama a la función responsable de analizar el sentimiento
response = text_analytics.sentiment(documents = documents)

print("====== Analyze sentiment ======")
# Se imprime el resultado de cada documento
for document in response.documents:
     print("Document Id: ", document.id, ", Sentiment Score: ",
           "{:.2f}".format(document.score))
print("===============================\n\n")

################################# EXTRACT KEY PHRASES #################################

# Datos dummy
documents = [
    {
        "id": "1",
        "language": "ja",
        "text": "猫は幸せ"
    },
    {
        "id": "2",
        "language": "de",
        "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."
    },
    {
        "id": "3",
        "language": "en",
        "text": "My cat might need to see a veterinarian."
    },
    {
        "id": "4",
        "language": "es",
        "text": "A mi me encanta el fútbol!"
    }
]

# Se llama a la función para obtener las palabras claves
response = text_analytics.key_phrases(documents = documents)

# Se imprime los resultados
print("====== Extract Key Phrases ======")
for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Phrases:")
    for phrase in document.key_phrases:
        print("\t\t", phrase)
print("=================================\n\n")


################################# IDENTIFY ENTITES #################################

# Datos dummy
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800."
    },
    {
        "id": "2",
        "language": "es",
        "text": "La sede principal de Microsoft se encuentra en la ciudad de Redmond, a 21 kilómetros de Seattle."
    }
]

# Se llama a la función correspondiente
response = text_analytics.entities(documents = documents)

# Se imprimen los resultados
print("======= Identify Entities =======")
for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Entities:")
    for entity in document.entities:
        print("\t\t", "NAME: ", entity.name, "\tType: ",
              entity.type, "\tSub-type: ", entity.sub_type)
        for match in entity.matches:
            print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ",
                  "{:.2f}\n".format(match.entity_type_score))
print("=================================\n\n")

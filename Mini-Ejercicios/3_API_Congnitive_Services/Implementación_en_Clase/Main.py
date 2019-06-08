#-------------------------------------------------------------------------
# Script para ejemplificar la implementación de la clase Text Analytics.
#
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install --upgrade azure-cognitiveservices-language-textanalytics"
#   4-. Tener la clase de Text Analytics
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
#--------------------------------------------------------------------------

from TextAnalytics import TextAnalytics

# Una instancia de la clase hecha para facilitar el uso de
TA_Instancia = TextAnalytics("-", "-")


# Datos dummy
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "RT @starksual: the dusted avengers when dr strange opened all the portals in the final battle https://t.co/k4yhdWHZcN"
    },
    {
        "id": "2",
        "language": "th",
        "text": "RT @Marvel_TH: ภาพชุดใหม่จาก Avengers: Endgame https://t.co/lEXrZyxXJe"
    },
    {
        "id": "3",
        "language": "en",
        "text": "Big question @Marvel If X-men enter the fold... what in the hell does that mean for QuicksilverForeign Quicksil… https://t.co/8vU1nFtBU2"
    },
    {
        "id": "4",
        "language": "(Unknown)",
        "text": "🙈"
    }, 
    {
        "id": "5",
        "language": "en",
        "text": "Big question @Marvel If X-men enter the fold... what in the hell does that mean for QuicksilverForeign Quicksil… https://t.co/8vU1nFtBU2"
    }
]

# Se llama la función para detectar los lenguajes
response = TA_Instancia.detectLanguages(documents)

# Como regresa un arreglo, hay que recorrerlo
print("======= Detect languages ======")
for document in response.documents:
    # Se imprime el resultado de cada documento
    print("Document Id: ", document.id, ", Language: ",
          document.detected_languages[0].iso6391_name)
print("===============================\n\n")


# Se analiza el sentimiento
response = TA_Instancia.analyzeSentiment(documents)

# Se imprime el resultado de cada documento
print("====== Analyze sentiment ======")
for document in response.documents:
    print("Document Id: ", document.id, ", Sentiment Score: ",
            "{:.2f}".format(document.score))
print("===============================\n\n")


# Se analiza las frases clave
response = TA_Instancia.keyPhrases(documents)

# Se imprime los resultados
print("====== Extract Key Phrases ======")
for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Phrases:")
    for phrase in document.key_phrases:
        print("\t\t", phrase)
print("=================================\n\n")


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

# Se obtiene las entidades
response = TA_Instancia.identifyEntites(documents)

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

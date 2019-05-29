from TextAnalytics import TextAnalytics

# Una instancia de la clase hecha para facilitar el uso de
TA_Instancia = TextAnalytics("8c5fb6709dc0410384e8fdb8da42a76f", "eastus")


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

# Se llama la función para detectar los lenguajes
response = TA_Instancia.detectLanguages(documents)

# Como regresa un arreglo, hay que recorrerlo
print("======= Detect languages ======")
for document in response.documents:
    # Se imprime el resultado de cada documento
    print("Document Id: ", document.id, ", Language: ",
            document.detected_languages[0].name)
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

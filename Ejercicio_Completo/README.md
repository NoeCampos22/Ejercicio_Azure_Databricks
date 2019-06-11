# Ejercicio Completo

Esta es la solución completa al ejercicio para el análisis de sentimiento de Tweets.

### Scripts Principales

- **TweetsMining.py:** Es el programa que sirve como web listener de Tweets. Se conecta a una aplicación de Twitter por medio de la API llamada Tweepy y cuando recibe un *objeto tweet* se queda solo con los atributos *"id"* y *"texto"* para finalmente mandarlo a un recurso llamado *Event Hub* de Microsoft Azure.

- **TweetsReceiver.py:** Programa que se encarga de conectarse al Event Hub para traerse los mensajes o eventos que estén disponibles y al mismo tiempo guarda un checkpoint en un blob storage para no repetir mensajes. Luego utiliza la librería de Cognitive Services Text Analytics, para así detectar el lenguaje, el puntaje del sentimiento, las palabras claves y las entidades detectadas en el texto de cada tweet. Finalmente, utiliza la librería de *Storage* de Azure para guardarlos en una *Table Storage*.

### Imports

- **Credentials.py:** Archivo que contiene todas las llaves y strings necesarios para conectarse a la API de Twitter o a los diferentes recursos de Azure que se utilizan.

- **simplerTweets.py:** Es un archivo que contiene una clase muy sencilla para guardar el ID y el texto de cada objeto tweet.

- **TableStorage.py:** Para facilitar el uso de la biblioteca hecha por Microsoft Azure, hice esta clase que resume las líneas necesarias para crear la conexión con el *storage account* y para interactuar con las tablas.

- **TextAnalytics.py:** De la misma manera, hice esta clase con la intención de facilitar el uso de los recursos proporcionados por Azure.

## Links de Ayuda
- [Twitter Developer Apps](https://developer.twitter.com/en/docs/basics/apps/overview.html)
- [Tweepy](https://www.tweepy.org/)
- [Objeto Tweet](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html)
- [Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about)
- [Send events to or receive events from Event Hubs using Python](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send#send-events)
- [Call the Text Analytics Service using the Python SDK](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python-sdk#language-detection)
- [Get started with Azure Table storage and the Azure Cosmos DB Table API using Python](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python#create-an-azure-service-account)
- [Examples Storage Code](https://github.com/Azure-Samples/storage-table-python-getting-started/blob/master/table_basic_samples.py)

# Mini Ejercicios

Como nunca había trabajado con los recursos de Azure de esta manera decidí realizar mini ejercicios donde implemente y practique con cada recurso de manera individual.

- **Enviar_Recibir_Eventos_EventHub:** 
    - ***Sender.py:*** Es donde puse en práctica el enviar N eventos con una estructura JSON como mensaje. 
    - ***Receiver.py*** Se encarga de leer TODOS los eventos que contiene el Event Hub.
    - ***EPH.py:*** A diferencia del script anterior, este sirve para leer los eventos, pero dejar un *checkpoint* para no repetir la lectura de eventos.

- **Guardar_en_Storage:** 
    - ***Ejemplo Microsoft:*** Descargué y corrí una implementación que el mismo Microsoft brinda como ejemplo.
    - ***Implementación Clase:*** Hice una clase para facilitar el uso del recurso de storage de Azure y la implementé en un *Main.py* como ejemplo.

- **API_Cognitive_Services:** 
    - ***Ejemplo Microsoft:*** Descargué y corrí una implementación que el mismo Microsoft brinda como ejemplo.
    - ***Implementación Clase: *** Hice una clase para facilitar el uso del recurso de storage de Azure y la implementé en un *Main.py* como ejemplo.

- ***Tweets_Mining:*** Es un programa que desarrolle para traerse los tweets que pasen el filtro especificado.


## Links de Ayuda
- [Twitter Developer Apps](https://developer.twitter.com/en/docs/basics/apps/overview.html)
- [Tweepy](https://www.tweepy.org/)
- [Objeto Tweet](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html)
- [Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about)
- [Send events to or receive events from Event Hubs using Python](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send#send-events)
- [Call the Text Analytics Service using the Python SDK](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python-sdk#language-detection)
- [Get started with Azure Table storage and the Azure Cosmos DB Table API using Python](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python#create-an-azure-service-account)
- [Examples Storage Code](https://github.com/Azure-Samples/storage-table-python-getting-started/blob/master/table_basic_samples.py)

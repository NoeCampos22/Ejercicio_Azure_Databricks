# Análisis de Sentimiento de Tweets 

Es un ejercicio hecho en Python 3.6.7 que se encarga de minar Tweets con la [API Tweepy](https://www.tweepy.org/) y analizar el sentimiento del texto.
Para realizar esto es necesario tener una subscripción de Microsoft Azure, crear un grupo de recursos y crear los siguientes recursos:
- Event Hub
- Text Analytics
- Storage Account

Este ejercicio está basado en tutorial [Sentiment analysis on streaming data using Azure Databricks](https://docs.microsoft.com/en-us/azure/azure-databricks/databricks-sentiment-analysis-cognitive-services) de Microsoft Azure, pero no tomé en cuenta al recurso Databricks y por ello son scripts o programas de consola.

## Directorio: Ejercicio Completo

Es donde está el programa para minar tweets y el necesario para obtenerlos, analizarlos y guardar los resultados.


## Directorio: Mini-Ejercicios

Contiene subdirectorios que guardan ejercicios e implementaciones de los diferentes pasos y procesos necesarios para realizar el ejercicio completo.

## Instalaciones Necesarias
Para hacer funcionar estos scripts en necesario que cuentes con:
- Python 3.6
- Instalador pip
```Python
python3 get-pip.py 
```
- [Tweepy API](https://pypi.org/project/tweepy/)
```Python
pip3 install tweepy
```
- [SDK de azure-eventhub](https://pypi.org/project/azure-eventhub/)

```Python
pip3 install azure-eventhub
```
- [SDK de azure-storage](https://pypi.org/project/azure-storage/)

```Python
pip3 install azure-storage
```
- [SDK Text Analytics](https://pypi.org/project/azure-cognitiveservices-language-textanalytics/)
```Python
pip install --upgrade azure-cognitiveservices-language-textanalytics
```


## Links de Ayuda
- [Twitter Developer Apps](https://developer.twitter.com/en/docs/basics/apps/overview.html)
- [Tweepy](https://www.tweepy.org/)
- [Objeto Tweet](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html)
- [Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about)
- [Send events to or receive events from Event Hubs using Python](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send#send-events)
- [Call the Text Analytics Service using the Python SDK](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python-sdk#language-detection)
- [Get started with Azure Table storage and the Azure Cosmos DB Table API using Python](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python#create-an-azure-service-account)
- [Examples Storage Code](https://github.com/Azure-Samples/storage-table-python-getting-started/blob/master/table_basic_samples.py)

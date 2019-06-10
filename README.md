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
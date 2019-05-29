##############################################################################
##  Mini script para poner ejemplos de como utlizar la clase TableStorage   ##
##############################################################################

import json
from TableStorage import TableStorage

# El string de conexión al storage account
ConnectionString = 'DefaultEndpointsProtocol=https;AccountName=stgeducon;AccountKey=ZSiqHjaX+3yooxOVZbffjbjaKnlMHWyYHBtxH2ANxle3EDMSqZ66cd75HUT0Tr48QPYRJus7XkwPT6aJ2wrAyQ==;EndpointSuffix=core.windows.net'

# Crea una instancia del objecto Table Storage
TableStorage = TableStorage(ConnectionString)

# Crea una Table service
TableStorage.CreateTableServices()

# Crea una tabla con el nombre "Tabla"
TableStorage.createTable('Tabla')

# Agrega 50 objetos
for iI in range(0, 50):
    Object = "{ \"PartitionKey\": \"PK" + str(iI) + "\", \"RowKey\": \"RK" + str(
        iI) + "\", \"Mensaje\": \"asaasdsadsads" + str(iI) + "\", \"Nombre\": \"Noe\"}"

    ObjectParsed = json.loads(Object)
 
    TableStorage.insertEntity('Tabla', ObjectParsed)
    print(Object)



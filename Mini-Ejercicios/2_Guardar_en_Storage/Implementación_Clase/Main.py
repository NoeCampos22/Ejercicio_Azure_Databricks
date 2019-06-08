#-------------------------------------------------------------------------
# Script corto donde se ejemplefica la implementación de la clase 
# TableStorage ubicada en el mismo directorio que este.
#
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install azure-storage"
#
# Autor: Noé Amador Campos Castillo.
# E-mail: noecampos@tec.mx
#--------------------------------------------------------------------------

import json
from TableStorage import TableStorage

# El string de conexión al storage account
ConnectionString = '--'

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



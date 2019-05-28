#-------------------------------------------------------------------------
# Clase para crear una conexión y poder hacer uso 
# del funciones en un Storage Account, especificamente para Table Storage.
#  
# Instrucciones para utilizarla.
#   1-. Tener Python 3.4 o mayor.
#   2-. Tener el instalador de paquetes "pip".
#   3-. Ingresar el comando "pip install azure-storage"
#   4-. Listo
#
# Author: Noé Amador Campos Castillo.
# E-mail: noecampos@hotmail.com
#--------------------------------------------------------------------------

from azure.storage import CloudStorageAccount
from azure.storage.table import TableService, Entity

# Clase para crear una instancia de TableServices y usar sus funciones
class TableStorage():

    """
    Constructor. Espera el Connection String del Azure Storage Account.
    Se obtiene ingresando al recurso de Storage -> Access Keys

    Parametros:
        CONNECTION_STRING   = El string que incluye el AccountName, 
                              AccountKey y el EndPointSuffix
    """
    def __init__(self, CONNECTION_STRING):
        self.CONNECTION_STRING = CONNECTION_STRING

        # Separa por partes el string de conexión
        Config = dict(s.split('=', 1)
                      for s in CONNECTION_STRING.split(';') if s)

        # Obtiene el nombre de la cuenta de storage y en EndpointSuffix
        self.AccountName = Config.get('AccountName')
        self.EndPointSuffix = Config.get('EndpointSuffix')


    def CreateTableServices(self):
        """
        Inicializa una instancia del Table Services para poder comunicarse con 
        el storage en Azure
        """
        self.TableService = TableService(account_name=self.AccountName,
                                         connection_string=self.CONNECTION_STRING,
                                         endpoint_suffix=self.EndPointSuffix)

    def createTable(self, TableName):
        """
        Revisa si la tabla no exista ya y la crea. De lo contrario, avisa que ya existe.

        Paramentros:
            TableName   = Nombre de la tabla que se quiere crear
        """
        print('\nCreate a table with name - ' + TableName)
    
        if(self.TableService.exists(TableName) != True):
            self.TableService.create_table(TableName)
            print("Table created succesfully!")
        else:
            print('Error creating table, ' + TableName + ' check if it already exists')

    def insertEntity(self, TableName, Entity):
        """
        Se inserta una entidad a la tabla especificada.

        Paramentros:
            TableName   = Nombre de la tabla que se quiere crear
            Entity      = El objecto con la entidad que se quiere agregar
        """
        print('\nInserting a new entity into table - ' + TableName)
        self.TableService.insert_or_merge_entity(TableName, Entity)
        print('Successfully inserted the new entity')

    def getEntity(self, TableName, PartitionKey, RowKey):
        """
        Traerse la entidad completa en base a la Partition Key y Row Key.
        
        Regresa un objeto como tal, no hay que hacer json.loads()
        
        Paramentros:
            TableName       = Nombre de la tabla que se quiere crear
            PartitionKey    = String con la partition key de la entidad deseada
            RowKey          = String con la row key de la entidad deseada
        """
        print('\nGetting entity.')
        Entity = self.TableService.get_entity(TableName, PartitionKey, RowKey)
        return Entity

    def updateEntity(self, TableName, NewEntity):
        """
        Toma el objeto con los datos actualizados y hace update en la table storage.
        
        Paramentros:
            TableName   = Nombre de la tabla que se quiere crear
            NewEntity   = El objecto con la entidad que se quiere hacer update
        """
        print('\nUpdating entity. PK: ' + NewEntity.PartitionKey + '  RK: ' + NewEntity.RowKey)
        self.TableService.update_entity(TableName, NewEntity)

    def deleteEntity(self, TableName, PartitionKey, RowKey):
        """
        Borrar la entidad que coincida en Partition Key y Row Key
        
        Paramentros:
            TableName       = Nombre de la tabla que se quiere crear
            PartitionKey    = String con la partition key de la entidad
            RowKey          = String con la row key de la entidad
        """
        print('\nDeleting entity')
        self.TableService.delete_entity(TableName, PartitionKey, RowKey)

    def deleteTable(self, TableName):
        """
        Revisa si la tabla existe y la borra, en caso contrario solo avisa que no existe.

        Paramentros:
            TableName   = Nombre de la tabla que se quiere borrar
        """
        print('\nDeleting the table.')
        if(self.TableService.exists(TableName)):
            self.TableService.delete_table(TableName)
            print('Successfully deleted the table')
        else:
            print('The table does not exists')


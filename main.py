from DATA.Mongodb import Mongodb
from API.Api import Api

# database operations
database = Mongodb()
database.get_database()
db_col = database.create_Col()

# database insert operations
products = Api()
#database.insert_db(products.get_products)

# database delete operations
database.delete_db_value(2)
# database 10-15 delete
for i in range(10,16):
    database.delete_db_value(i)

# database update operaitons
database.update_db_value(3, 'title', "muhammed_cbkc")
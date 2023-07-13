from API.Api import Api
from pymongo import MongoClient

class Mongodb(Api):
   def get_database(self):
        # Database connection
        CONNECTION_STRING = "mongodb://localhost:27018/"
        client = MongoClient(CONNECTION_STRING)

        # Create database
        return client['Products']

#  Create collections
   def create_Col(self):
       db_name = self.get_database()
       collection_name = db_name['Product']
       return collection_name

# database insert functions
   def insert_db(self,value):
       db_col = self.create_Col()
       if len(value) == 1:
           insert = db_col.insert_one(value)
       if len(value) > 1:
           insert = db_col.insert_many(value)
       return insert

# database delete functions
   def delete_db_value(self, id):
       db_col = self.create_Col()
       for value in Api.get_products:
         if value['id'] == id:
            db_col.delete_one(value)

# database update value functions
   def update_db_value(self,id, feature,new_value):
        db_col = self.create_Col()
        for value in Api.get_products:
            if 'id' == feature and value['id'] == id :
                filter = {'id': id}
                newvalues = {"$set": {'id': new_value}}
                db_col.update_one(filter,newvalues)
            if 'title' == feature:
                if value['id'] == id:
                    filter = {'id' : id}
                    newvalues = {"$set": {'title' : new_value}}
                    db_col.update_one(filter,newvalues)

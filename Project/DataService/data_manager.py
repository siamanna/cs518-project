"""
This is a reST style.

:param param_1: this is the first parameter
:param param_2: this is the second parameter
:returns: this is a description of what is returned
:raises keyError: raises an exception

"""

# pymongo allows python to speak with mongoDB
import pymongo
import sys
import unittest

# use a global variable to store your collection object
mycol = None

"""
Connect to the local MongoDB server, database, and collection.

"""

'''
initialize() 	
Establish a connection to the local MongoDB server
Create a database (any name is fine)
Create a collection (any name is fine) and assign it to global variable mycol
All done
'''
def initialize():
    # specify that we are using the global variable mycol
    global mycol

    #########################
    # INSERT YOU CODE BELOW #
    #########################

    # connect to your local mongoDB server
    my_client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)

    # check for a successful connection
    try:
        my_client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print("Connection timed out, please check if your mongod is running!")
        sys.exit(1)

    # create a database named 'mydatabase'
    my_database = my_client["mydatabase"]

    # list databases
    print("INTIALIZE(): List Database Names")
    print(my_client.list_database_names())

    # create a collection named 'mycollection'
    my_collection = my_database['mycollection']
    #assign it to a local variable "mycol"
    mycol = my_collection
    print("INITIALIZE(): List collection names")
    print(my_database.list_collection_names())




"""
Drop the collection and reset global variable mycol to None.

"""


def reset():
    # specify that we are using the global variable mycol
    global mycol

    #########################
    # INSERT YOU CODE BELOW #
    #########################
    #drop the collection
    #my_collection.drop()
    mycol.drop()
    #reset global variable mycol to None
    mycol = None
    # for d in mycol.find():
    #     print(d)


"""
Insert document(s) into the collection.

:param document: a Python list of the document(s) to insert
:returns: result of the operation

"""


def create(document):


    #########################
    # INSERT YOU CODE BELOW #
    #########################
    #if (len(document) == 1):
    #    return mycol.insert_one(document)
    #print("CREATE()")
    #return mycol.insert_many(document)



    #insert a list of document(s) into the collection
    #x = mycol.insert_many(document)
    #print("CREATE()")
    #print(x.inserted_ids)
    #return mycol
    print("CREATE(): \n")
    if isinstance(document, list):
        return mycol.insert_many(document)
    elif isinstance(document, dict):
        return mycol.insert_one(document)

"""
Retrieve document(s) from the collection that match the query,
if parameter one is True, retrieve the first matched document,
else retrieve all matched documents.

:param query: a Python dictionary for the query
:param one: an indicator of how many matched documents to be retrieved, by default its value is False
:returns: all matched document(s)

"""


def read(query, one=False):

    #########################
    # INSERT YOU CODE BELOW #
    #########################

    #mycol.forEach(document)
    # for document in mycol.find(query):
    #     if document == query:
    #         one = True
    #         print(d.get(query))
    #     else:
    #         one = False
    #         #return document

        if one:
            # Retrieve the first matched document
            print("READ(ONE = TRUE)")
            return mycol.find_one(query)
        else:
            # Retrieve all matched documents
            print("READ(ONE = FALSE)")
            return list(mycol.find(query))


"""
Update document(s) that match the query in the collection with new values.

:param query: a Python dictionary for the query
:param new_values: a Python dictionary with updated data fields / values
:returns: result of the operation

"""


def update(query, new_values):

    #########################
    # INSERT YOU CODE BELOW #
    #########################

    return mycol.update_many(query, {'$set': new_values})

    #testing
    #print("UPDATE():")
    #for d in mycol.find(new_values):
    #    print(d.get(query))
    #if document == query:
    #    document.insertMany(new_values)


"""
Remove document(s) from the collection that match the query.

:param query: a Python dictionary for the query
:returns: result of the operation

"""


def delete(query):


    #########################
    # INSERT YOU CODE BELOW #
    #########################

    mycol.delete_many(query)
    #if document == query:
    #    mycol.deleteOne(document)


if __name__ == "__main__":
    # sample tests
    initialize()

    create([{'title' : 'test', 'name': 'John', 'address': 'Highway 37'}])
    doc = read({}, one=True)
    print(doc)

    update({'title': 'test'}, {'address': "testing 3 4"})
    doc = read({}, one=True)
    print(doc)

    delete({'title': 'test'})
    doc = read({}, one=True)
    print(doc)

    reset()

    #########################
    # INSERT YOU TESTS BELOW #
    #########################
class intializeTests(unittest.TestCase):
    def testinitialize(self):
        initialize()

        documents = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 28}
        ]

        create(documents)

        query = {"age": {"$gte": 28}}
        result = read(query)
        print("Read Result:", result)

        update_query = {"name": "Alice"}
        new_values = {"age": 31}
        update(update_query, new_values)

        delete_query = {"name": "Bob"}
        delete(delete_query)

        reset()

        #update()


    
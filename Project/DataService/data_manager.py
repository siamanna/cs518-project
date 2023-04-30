import ssl

from pymongo import MongoClient

# use a global variable to store your collection object
my_col = None

# define connection string for atlas cluster
username = "cs518"
password = "ltgDm6reWuHh2m5E"
connection_url = "database.urwehi7.mongodb.net"
conn_str = f"mongodb+srv://{username}:{password}@{connection_url}"

# my_col accessor for testing
def get_mycol():
    global my_col
    if my_col is None:
        initialize()
    return my_col

# Connect to the atlas cluster
def initialize():
    global my_col
    client = MongoClient(conn_str)
    my_col = client["database"]["collection"]


# Drop the collection and reset global variable my_col to None.
def reset():
    global my_col
    get_mycol().drop()
    my_col = None


"""
Insert document(s) into the collection.
:param document: a Python list of the document(s) to insert
:returns: result of the operation
"""
def create(document):
    value = None
    if isinstance(document, list):
        for doc in document:
            value = get_mycol().insert_one(doc)
    else:
        value = get_mycol().insert_one(document)
    return str(value.inserted_id)

"""
Retrieve document(s) from the collection that match the query,
if parameter one is True, retrieve the first matched document,
else retrieve all matched documents.
:param query: a Python dictionary for the query
:param one: an indicator of how many matched documents to be retrieved, by default its value is False
:returns: all matched document(s)
"""
def read(query, one=False):
    if one:
        if len(query) == 0: return get_mycol().find_one()
        else: return get_mycol().find_one(query)
    else:
        if len(query) == 0: return list(get_mycol().find())
        else: 
            return list(get_mycol().find(query))
            # global my_col
            # while my_col is None:
            #     initialize()
            # results = my_col.find(query)
            # result_list = list(results)
            # return result_list


"""
Update document(s) that match the query in the collection with new values.
:param query: a Python dictionary for the query
:param new_values: a Python dictionary with updated data fields / values
:returns: result of the operation
"""
def update(query, new_values):
    return get_mycol().update_many(query, {'$set': new_values})

"""
Remove document(s) from the collection that match the query.
:param query: a Python dictionary for the query
:returns: result of the operation
"""
def delete(query):
    return get_mycol().delete_many(query)



# for testing
def count_documents():
    return get_mycol().count_documents({})





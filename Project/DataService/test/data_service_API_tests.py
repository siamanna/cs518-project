import requests
import unittest
import json
import pymongo
import data_manager

username = "cs518"
password = "ltgDm6reWuHh2m5E"
auth_token = f"{username}:{password}"
create_url = "https://dataservice1234.azurewebsites.net/api/createrecord"
read_url = "https://dataservice1234.azurewebsites.net/api/readrecord"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
}


def filter_json_with_mongodb(json_, query):
    # Parse the JSON string into a Python dictionary
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]
    collection.drop()
    if isinstance(json_, list):
        for e in json_:
            collection.insert_one(document=e)
    else:
        collection.insert_one(json_)
    return list(collection.find(query))

def get(json_, test):
    [id, status] = execute_post(test_documents, test)
    if status != 200:
        return [id, status]
    return execute_get(json_, test, id)


def execute_get(json_, test, id):
    response = requests.get(read_url, params={'test': test}, headers=headers)
    body = json.loads(response.content)
    new_doc = {test: {}}
    for element in body:
        if element['_id']['$oid'] == id:
            new_doc = element['doc']
            break
    v = filter_json_with_mongodb(new_doc, json_)
    return [v, response.status_code]


def execute_post(json_, test):
    post_response = requests.post(create_url, json=[{'test': test, 'doc': json_}], headers=headers)
    return [json.loads(post_response.content)['id'], post_response.status_code]


# Define some test data
test_documents = [{'name': 'Alice', 'age': 30},
                  {'name': 'Bob', 'age': 25},
                  {'name': 'Alex', 'age': 35}]

class TestDataServiceAPI(unittest.TestCase):
    def test_create(self):
        # Test that documents are inserted into the collection
        [id, status] = execute_post(test_documents, 'test_create')
        self.assertEqual(200, status)
        [result, status] = execute_get({}, 'test_create', id)
        self.assertEqual(200, status)
        self.assertEqual(3, len(result))

    def test_read_all(self):
        # Test that all documents are retrieved from the collection
        [body, status] = get({}, 'test_read_all')
        self.assertEqual(200, status)
        self.assertEqual(3, len(body))

    def test_read_one(self):
        # Test that we can find the person that has an age of 30
        [body, status] = get({"age": 30}, 'test_read_one')
        self.assertEqual(200, status)
        self.assertEqual(1, len(body))
        self.assertEqual('Alice', body[0].get('name'))

    def test_read_filter_string(self):
        # Test that we can filter names starting with the letter A
        [body, status] = get({"name": {"$regex": "^A"}}, 'test_read_filter_string')
        self.assertEqual(200, status)
        self.assertEqual(2, len(body))
        self.assertEqual('Alice', body[0]['name'])
        self.assertEqual('Alex', body[1]['name'])

    def test_read_filter_int(self):
        # Test that we can filter ages over 25
        [body, status] = get({"age": {"$gt": 25}}, 'test_read_filter_int')
        self.assertEqual(200, status)
        self.assertEqual(2, len(body))
        self.assertEqual('Alice', body[0]['name'])
        self.assertEqual('Alex', body[1]['name'])


if __name__ == '__main__':
    result = data_manager.read({ "title": { "$regex": "hunger", "$options": "i" } })
    print(result)
    #unittest.main()

import csv
from fields import fields
import requests
import data_manager

filename = "test\\books_dataset.csv"

username = "cs518"
password = "ltgDm6reWuHh2m5E"
auth_token = f"{username}:{password}"
create_url = "https://dataservice12345.azurewebsites.net/api/CreateRecord"
read_url = "https://dataservice12345.azurewebsites.net/api/ReadRecord"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
}

def csv_to_dict_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        result = []
        for row in reader:
            result.append(row)
        return result

if __name__ == "__main__":
    result = csv_to_dict_list(filename)
    for dict in result: 
        post_response = requests.post(create_url, json=dict, headers=headers)
        print(post_response)

    print('done')
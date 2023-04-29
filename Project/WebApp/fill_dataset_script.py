import csv
from fields import fields
import requests

filename = "books_dataset.csv"
create_url = "https://dataservice12345.azurewebsites.net/api/CreateRecord"

headers = {
    'x-functions-key': 'k1_Oc5HUEf-R7L9SEFim75fUnmHl5efJwmAG73LdsvhxAzFuxIuW8w==',
    'Content-Type': 'application/json'
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
    # new_records_list_filtered = []

    # for d in result:
    #     new_dict = {}
    #     for k, v in d.items():
    #         if k.lower() in fields:
    #             new_dict[k.lower()] = v
    #     if any(f.lower() in new_dict.keys() for f in fields):
    #         new_records_list_filtered.append(new_dict)
            
    for dict in result: 
        response = requests.post(create_url, headers=headers, data=dict)
        if response.status_code == 200:
            print('successful')

    print('done')
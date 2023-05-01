import csv
from fields import fields
import requests
import data_manager

filename = "test\\books_dataset.csv"
num_to_insert = 1000

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
            r = {}
            for k, v in row.items():
                if k.lower() == 'coverimg':
                    r[k.lower()] = v
                else:
                    r[k.lower()] = v.lower()
            result.append(r)
        return result

def iterate():
    result = csv_to_dict_list(filename)
    count = 0
    for dict in result: 
        count = count + 1
        if (count > num_to_insert):
            return ''
        post_response = requests.post(create_url, json=dict, headers=headers)
        print(post_response)
    

if __name__ == "__main__":
    result = csv_to_dict_list(filename)
    iterate()
    print('done')
    
    
    
def csv_to_dict_list(filename):
    # Open the CSV file and read it as a dictionary
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        result = []
        # Iterate over each row in the CSV file
        for row in reader:
            r = {}
            # Iterate over each key-value pair in the row dictionary
            for k, v in row.items():
                # If the key is 'coverimg', add it to the dictionary
                # without modifying the value
                if k.lower() == 'coverimg':
                    r[k.lower()] = v
                # Otherwise, convert the value to lowercase and add it
                # to the dictionary
                else:
                    r[k.lower()] = v.lower()
            # Append the modified row dictionary to the result list
            result.append(r)
        # Return the list of dictionaries
        return result

def insert_data():
    # Convert the CSV file to a list of dictionaries
    result = csv_to_dict_list(filename)
    # Initialize a counter to keep track of the number of rows inserted
    count = 0
    # Iterate over the first `num_to_insert` rows in the list
    for row in result[:num_to_insert]:
        # Send a POST request to the API endpoint with the row dictionary
        # as the JSON payload and the headers
        post_response = requests.post(create_url, json=row, headers=headers)
        # Print the response from the API endpoint
        print(post_response)
        # Increment the counter
        count += 1
        # Exit the loop if the counter is greater than or equal to `num_to_insert`
        if count >= num_to_insert:
            break

if __name__ == "__main__":
    # Convert the CSV file to a list of dictionaries
    result = csv_to_dict_list(filename)
    # Call the insert_data() function to insert the data into the API
    insert_data()
    # Print 'Done' when the script is finished
    print('Done')
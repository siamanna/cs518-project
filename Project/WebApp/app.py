from flask import Flask, render_template
import requests
import json


username = "cs518"
password = "ltgDm6reWuHh2m5E"
auth_token = f"{username}:{password}"
create_url = "https://dataservice1234.azurewebsites.net/api/createrecord"
read_url = "https://dataservice1234.azurewebsites.net/api/readrecord"
search_query = {}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
}


app = Flask(__name__, template_folder='/templates')


@app.route('/records')  # create a new route for /records endpoint
def records():

    # send a GET request to read record API
    response = requests.get(read_url, params=search_query, headers=headers)

    # parse the JSON response into a Python list of dictionaries
    records_dict = json.loads(response.content)

    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=records_dict)


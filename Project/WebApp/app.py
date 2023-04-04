from flask import Flask, render_template
import requests
from bson import json_util

app = Flask(__name__)
create_url = "https://dataservice1234.azurewebsites.net/api/createrecord"
read_url = "https://dataservice1234.azurewebsites.net/api/readrecord"


@app.route('/records')  # create a new route for /records endpoint
def records():
    # send a GET request to read record API
    response = requests.get(read_url)

    # parse the JSON response into a Python list of dictionaries
    records = json_util.loads(response.text)

    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=records)
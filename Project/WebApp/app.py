from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import os


create_url = "https://dataservice12345.azurewebsites.net/api/CreateRecord"
read_url =   "https://dataservice12345.azurewebsites.net/api/ReadRecord"
search_query = {}


headers = {
    'x-functions-key': 'k1_Oc5HUEf-R7L9SEFim75fUnmHl5efJwmAG73LdsvhxAzFuxIuW8w==',
    'Content-Type': 'application/json'
}

# define a route for the root URL '/'
app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/records', methods=['GET'])  # create a new route for /records endpoint
def records():

    # send a GET request to read record API
    response = requests.get(read_url, params=search_query)

    # parse the JSON response into a Python list of dictionaries
    records_dict = json.loads(response.content)
    # records_dict = {"test": "test"}

    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=records_dict)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form.to_dict()
        data = json.dumps(data)
        response = requests.post(create_url, headers=headers, data=data)
        if response.status_code == 200:
            return redirect(url_for('records'))
    return render_template('create.html')

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()

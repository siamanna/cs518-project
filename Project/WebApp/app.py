from flask import Flask, render_template
import requests
import json
import os



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

# define a route for the root URL '/'
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return 'Welcome to my Flask App!'

@app.route('/records')  # create a new route for /records endpoint
def records():

    # send a GET request to read record API
    response = requests.get(read_url, params=search_query, headers=headers)

    # parse the JSON response into a Python list of dictionaries
    records_dict = json.loads(response.content)

    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=records_dict)

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()

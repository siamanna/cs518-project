from flask import Flask, render_template, redirect, url_for, request
from fields import fields, length, display
import requests
import json
import os


create_url = "https://dataservice12345.azurewebsites.net/api/CreateRecord"
read_url = "https://dataservice12345.azurewebsites.net/api/ReadRecord"
delete_url = "https://dataservice12345.azurewebsites.net/api/DeleteRecord"
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
    records_list = json.loads(response.content)
    records = []

    for d in records_list:
        num_fields = 0
        new_dict = {}
        for k, v in d.items():
            if k.lower() in fields:
                if (v != 'sdf' and v != ''):
                    num_fields = num_fields + 1
                max = length[k.lower()]
                v = v.replace('[', '').replace(']', '').replace('\'', '')
                if k.lower() == 'description':
                    v = v.lower()
                v = v[:max] + '...' if len(v) > max else v
                new_dict[k.lower()] = v
        if new_dict:
            if num_fields > 8:
                records.append(new_dict)

    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=records, fields=fields, display=display)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form.to_dict()
        data = json.dumps(data)
        response = requests.post(create_url, headers=headers, data=data)
        if response.status_code == 200:
            return redirect(url_for('records'))
    return render_template('create.html', fields=fields)


@app.route('/search', methods=['GET', 'POST'])  # create a new route for /records endpoint
def search():
    if request.method == 'GET':
        return render_template('search.html', fields=fields)
        
    data = request.form.to_dict()
    
    search_q = {}
    for k, v in data.items():
        if v != '':
            search_q[k] = v
    
    # send a GET request to read record API
    response = requests.get(read_url, params=search_q)

    # parse the JSON response into a Python list of dictionaries
    records_list = json.loads(response.content)
    records = []

    for d in records_list:
        num_fields = 0
        new_dict = {}
        for k, v in d.items():
            if k.lower() in fields:
                if (v != 'sdf' and v != ''):
                    num_fields = num_fields + 1
                v = v.replace('[', '').replace(']', '').replace('\'', '')
                v = v[:45] + '...' if len(v) > 45 else v
                new_dict[k.lower()] = v
        if new_dict:
            if num_fields > 8:
                records.append(new_dict)
                
    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=records, fields=fields)

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    print(request.method)
    if request.method == 'DELETE':
        data = request.form.to_dict()
        data = json.dumps(data)
        response = requests.delete(delete_url, headers=headers, data=data)
        if response.status_code == 200:
            return redirect(url_for('records'))
    return render_template('delete.html', fields=fields)

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()


from flask import Flask, render_template, request, redirect, url_for
from bson import json_util
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        # Render the form template
        return render_template(('create.html'))
    elif request.method == 'POST':
        # Do something with the form data, e.g. save it to a database
        id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        
        payload = {'ID': id, 'Name': name, 'PhoneNumber': phone}
        response = requests.post('https://cs518lab.azurewebsites.net/api/createrecord', json = payload)

        if response.status_code == 200:
            return redirect(url_for('records'))
        # Redirect to a page to confirm the record was created
        else:
            return "Error creating record"
    

@app.route("/records")
def records():
    response = requests.get("https://cs518lab.azurewebsites.net/api/readrecords")
    records = json_util.loads(response.text)
    return render_template("records.html", records = records)

from flask import Flask, render_template, redirect, url_for, request
from fields import fields, browse_categories
import requests
import json
import os
import re


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


@app.route('/admin_home', methods=['GET', 'POST', 'PUT'])
def admin_home():
    fields['html']['title'] = 'Admin Home'
    if fields['admin']:
        return render_template('home.html', fields=fields)
    
    fields['admin'] = True
    return render_template('login.html', fields=fields)

@app.route('/public_home')
def public_home():
    fields['html']['title'] = 'Home'
    fields['admin'] = False
    return render_template('home.html', fields=fields)


@app.route('/browse')
def browse():
    return render_template('browse.html', browse_categories=browse_categories, fields=fields)

@app.route('/genres', methods=['GET', 'POST'])
def genres():
    return browse_category('genres', request)
    # if request.method == 'GET':
    #     category=browse_categories['genres']
    #     category['category']='genres'
    #     return render_template('category.html', category=category, fields=fields)
    
    # selections = request.form.getlist('selectedOptions[]')
    
    # options = []
    
    # for selection in selections:
    #     options.append({'genres':{"$regex": selection.lower()}})
        
    # search_q = {"$or": options}
            
    # response = requests.get(read_url, json=search_q)
    # records_list = json.loads(response.content)
    
    # # render the records.html template and pass in the records list as a variable
    # return render_template('records.html', records=clean_response(records_list), fields=fields)


def browse_category(category, request):
    if request.method == 'GET':
        category_=browse_categories[category]
        category_['category']=category
        return render_template('category.html', category=category_, fields=fields)
    
    selections = request.form.getlist('selectedOptions[]')
    
    options = []
    
    for selection in selections:
        if selection.lower() == 'all':
            return redirect(url_for('records'))
        options.append({category:{"$regex": selection.lower()}})
        
    search_q = {"$or": options}
            
    response = requests.get(read_url, json=search_q)
    records_list = json.loads(response.content)
    
    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=clean_response(records_list), fields=fields)

    

@app.route('/author', methods=['GET', 'POST'])
def author():
    return browse_category('author', request)

@app.route('/rating', methods=['GET', 'POST'])
def rating():
    if request.method == 'GET':
        category=browse_categories['rating']
        category['category']='rating'
        return render_template('category.html', category=category, fields=fields)

    selections = request.form.getlist('selectedOptions[]')
    options = []
    for selection in selections:
        if selection.lower() == 'all':
            return redirect(url_for('records'))
        if '1' in selection:
            options.append({'rating':{"$regex": '1'}})
        if '3' not in selection and '4' not in selection:
            options.append({'rating':{"$regex": '2'}})
        if '4' not in selection:
            options.append({'rating':{"$regex": '3'}})
        options.append({'rating':{"$regex": '4'}})
        options.append({'rating':{"$regex": '5'}})
        
    search_q = {"$or": options}
            
    response = requests.get(read_url, json=search_q)
    records_list = json.loads(response.content)
    
    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=clean_response(records_list), fields=fields)

@app.route('/records', methods=['GET'])  # create a new route for /records endpoint
def records():
    fields['html']['title'] = 'Library Catalog'

    # send a GET request to read record API
    response = requests.get(read_url, params=search_query)

    # parse the JSON response into a Python list of dictionaries
    records_list = json.loads(response.content)
    
    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=clean_response(records_list), fields=fields)



def clean_response(records_list):
    records = []
    for d in records_list:
        num_fields = 0
        new_dict = {}
        for k, v in d.items():
            if k.lower() in fields:
                if (v != ''):
                    num_fields = num_fields + 1
                max = fields[k.lower()]['max']
                v = v.replace('[', '').replace(']', '').replace('\'', '')
                v = v[:max] + '...' if len(v) > max else v
                new_dict[k.lower()] = v
        if new_dict:
            if num_fields > 8:
                records.append(new_dict)
    return records
                
@app.route('/create', methods=['GET', 'POST'])
def create():
    fields['html']['title'] = 'Create Record'
    if request.method == 'POST':
        data = request.form.to_dict()
        data = json.dumps(data)
        response = requests.post(create_url, headers=headers, data=data)
        if response.status_code == 200:
            return redirect(url_for('records'))
    return render_template('form.html', fields=fields)


@app.route('/search', methods=['GET', 'POST'])  # create a new route for /records endpoint
def search():
    fields['html']['title'] = 'Search Records'
    if request.method == 'GET':
        return render_template('form.html', fields=fields)
        
    data = request.form.to_dict()
    
    search_q = {}
    for k, v in data.items():
        if v != '':
            search_q[k] = {"$regex": v.lower()}
            
    # # pattern = re.compile('.*hunger games.*', re.IGNORECASE)
    # # search_q = {'title':{"$regex":"hunger games","$options":"i"}}
    # search_q = '{"title":{"$regex":"hunger games","$options":"i"}}'
    # # search_q = read_url + '{"title":{"$regex":"hunger games","$options":"i"}}'

    # search_q = {"title": {"$regex":"hunger games"}}
    # send a GET request to read record API
    response = requests.get(read_url, json=search_q)
    
    # response = requests.get(read_url, params=search_q)


    # parse the JSON response into a Python list of dictionaries
    records_list = json.loads(response.content)
    
    # render the records.html template and pass in the records list as a variable
    return render_template('records.html', records=clean_response(records_list), fields=fields)

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    fields['html']['title'] = 'Delete Record'
    print(request.method)
    if request.method == 'DELETE':
        data = request.form.to_dict()
        data = json.dumps(data)
        response = requests.delete(delete_url, headers=headers, data=data)
        if response.status_code == 200:
            return redirect(url_for('records'))
    return render_template('form.html', fields=fields)

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()

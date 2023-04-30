import json
from bson import json_util
import logging
import data_manager

import azure.functions as func

def parse_json(data):
    return json.dumps(json.loads(json_util.dumps(data)))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        body = req.get_json()
    except ValueError as e:
        try:
            body = req.params
        except ValueError as e:
            body = {}
    # query = {}
    # for k,v in body:
    #     if isinstance(v, str):
    #         query[k] = { "$regex": v, "$options": "i" }
    #     else:
    #         query[k] = v
    result = data_manager.read(body)
    return func.HttpResponse(body=parse_json(result), status_code=200)

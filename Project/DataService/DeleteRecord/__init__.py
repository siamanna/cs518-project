import azure.functions as func
import json
from bson import json_util
import logging
import data_manager

def parse_json(data):
    return json.dumps(json.loads(json_util.dumps(data)))


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    data_manager.initialize()
    val = data_manager.delete(req_body)
    result = {'id': val}
    return func.HttpResponse(body=parse_json(result), status_code=200)
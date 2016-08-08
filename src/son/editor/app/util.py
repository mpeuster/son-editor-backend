'''
Created on 28.07.2016

@author: Jonas
'''
import json

from flask.wrappers import Response
from pkg_resources import Requirement, resource_filename
import yaml

configFileName = resource_filename(Requirement.parse("sonata_editor"), "config.yaml")
CONFIG = yaml.safe_load(open(str(configFileName)))


def prepareResponse(data=None):
    response = Response()
    headers = response.headers
    headers['Access-Control-Allow-Origin'] = CONFIG["frontend-host"]
    headers['Access-Control-Allow-Methods'] = "GET,POST,PUT,DELETE,OPTIONS"
    headers['Access-Control-Allow-Headers'] = "Content-Type, Authorization, X-Requested-With"
    headers['Access-Control-Allow-Credentials'] = "true"
    headers['Access-Control-Max-Age'] = 1000
    if isinstance(data, str):
        response.set_data(data)
        headers['contentType'] = 'text/plain'
    elif data is not None:
        response.set_data(json.dumps(data))
        headers['contentType'] = 'application/json'
    response.headers = headers
    return response


def getJSON(request):
    jsonData = request.get_json()
    if jsonData is None:
        jsonData = json.loads(request.get_data().decode("utf8"))
    return jsonData

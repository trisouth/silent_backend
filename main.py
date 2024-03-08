#import json
#import os
#from pymongo import MongoClient
from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
from flask_restful import Api
from src import api_bp
from src.routes.routeManager import routeManager
#from dotenv import load_dotenv

import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set desired log level (e.g., INFO, WARNING)
    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
)



# if you store that app.py in the same level with templates directory use the below
# app4 definition.
app4 = Flask(__name__)

#CORS(app4, origins=['http://10.211.55.9:5173']) # when I disable firewall worked fine.
CORS(app4, origins=['http://10.211.55.9:5173', 'http://localhost:5173'], allow_headers=['Content-Type'], allow_methods=['GET', 'POST'])

# Replace with your desired log file
app4.logger.addHandler(logging.FileHandler('/var/log/nginx/app.log'))

# if you store that app.py in another directory within the project
# use the below app definition.
#app4 = Flask(__name__, template_folder='../../templates')

app4.register_blueprint(api_bp)

#mongo_client = MongoClient("mongodb://silentadmin:silentPass123@10.211.55.9:27017")
#mongo_silentdb = mongo_client.get_database("silentmon")
#mongo_silentcoll = mongo_silentdb.get_collection("users")

#app4.config["MONGO_CLIENT"] = mongo_client
#app4.config["MONGO_DB"] = mongo_silentdb
#app4.config["MONGO_COLL"] = mongo_silentcoll
app4.config["MONGO_COLL"] = "users"

app4.config["MONGO_URI"] = "mongodb://silentadmin:silentPass123@localhost:27017/silentmon"

api = Api(app4)

router = routeManager.RouteManager()

logger = logging.getLogger(__name__)

@app4.route('/')
def home():
    return render_template('index.html')

@app4.route('/hello', methods=['GET', 'POST'])
def hello_world():
    logger.info("hello_world() called")
    if request.method == 'POST':
        logger.info("hello_world() POST called")
        payload = request.json
        logger.info('This is the payload: ' + str(payload))

    response = jsonify({"message": "Hello World! Utku Guney"})
    #response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins (for development)
    # OR
    # response.headers.add('Access-Control-Allow-Origin', 'http://10.211.55.9:5173')  # Allow specific origin
    return response, 200


if __name__ == '__main__':
    app4.run(host='0.0.0.0')
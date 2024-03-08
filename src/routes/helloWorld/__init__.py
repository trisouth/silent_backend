from flask import Blueprint
from flask_restful import Api

hello_world_bp = Blueprint("helloWorld", __name__, url_prefix="/hello-world")
hello_world_api = Api(hello_world_bp)
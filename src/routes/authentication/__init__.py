## 004

from flask import Blueprint
from flask_restful import Api

authentication_blueprint_root = Blueprint("authentication_root", __name__)

authentication_api_root = Api(authentication_blueprint_root)
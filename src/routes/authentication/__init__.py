## 0.1.001

from flask import Blueprint
from flask_restful import Api

authentication_blueprint_root = Blueprint("authentication_root", __name__, url_prefix="/authentication")
authentication_blueprint_id = Blueprint("authentication_id", __name__, url_prefix="/authentication")

authentication_api_root = Api(authentication_blueprint_root)
authentication_api_id = Api(authentication_blueprint_id)
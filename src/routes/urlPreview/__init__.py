from flask import Blueprint
from flask_restful import Api

url_preview_blueprint = Blueprint("url-preview", __name__, url_prefix="/url-preview")
url_preview_api = Api(url_preview_blueprint)
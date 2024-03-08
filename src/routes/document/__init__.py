from flask import Blueprint
from flask_restful import Api


#document_blueprint_root = Blueprint("document_root", __name__, url_prefix="/document")

document_blueprint_root = Blueprint("document_root", __name__)

#document_blueprint_id = Blueprint("document_id", __name__, url_prefix="/document/<string:document_id>")
#document_blueprint_all = Blueprint('document_all', __name__, url_prefix='/document-all')

document_api_root = Api(document_blueprint_root)
#document_api_id = Api(document_blueprint_id)
#document_api_all = Api(document_blueprint_all)
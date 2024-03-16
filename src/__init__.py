from flask import Blueprint
from src.routes.helloWorld import hello_world_bp
from src.routes.document import document_blueprint_root #, document_blueprint_id, document_blueprint_all
from src.routes.authentication import authentication_blueprint_root, authentication_blueprint_id

#from src.routes.urlPreview import url_preview_blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api_bp.register_blueprint(hello_world_bp)

api_bp.register_blueprint(document_blueprint_root)

api_bp.register_blueprint(authentication_blueprint_root)
api_bp.register_blueprint(authentication_blueprint_id)

#api_bp.register_blueprint(document_blueprint_id)
#api_bp.register_blueprint(document_blueprint_all)

#api_bp.register_blueprint(url_preview_blueprint)
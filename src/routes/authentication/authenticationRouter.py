## 0.1.001

from src.controllers.authenticationController import AuthenticationRootController, AuthenticationIdController
from src.routes.authentication import authentication_api_root, authentication_api_id



class AuthenticationRouter:

    def __init__(self):
        authentication_api_root.add_resource(AuthenticationRootController, '/', endpoint='authentication_root') # /authentication
        authentication_api_id.add_resource(AuthenticationIdController, '/<string:user_id>', endpoint='authentication_id') # /authentication/<string:user_id>
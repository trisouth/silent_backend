## 2.1.001

import json
from flask import current_app, Response
from logging import getLogger

from flask import current_app, g

logger = getLogger(__name__)

class AuthenticationService:

    def __init__(self):
        pass

    def getAuthenticateByJson(self, request):

        try:
            json_payload = request.get_json()

            if 'username' in json_payload and 'password' in json_payload:
                return self.getAuthenticate(json_payload['username'], json_payload['password'])
            
            else:
                return Response(json.dumps({'Input error': 'invalid username or password'}), status=404, mimetype='application/json')
        
        except Exception as e:
            logger.error("Exception getAuthenticateByJson: \n json_payload: %s \n %s\n", json_payload, str(e))
            return Response(json.dumps({'Exception': '203'}), status=422, mimetype='application/json')
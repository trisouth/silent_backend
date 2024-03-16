## 1.001
from flask import render_template, make_response
from src.services.authenticationService import authenticationService
from flask_restful import Resource, request as restful_request
from logging import getLogger

logger = getLogger(__name__)

authentication_service = authenticationService.AuthenticationService()


class AuthenticationRootController(Resource):

    def get(self):

        try:
            browser_name = restful_request.headers.get('User-Agent')
            # Browser names:
            # Browser: PostmanRuntime/7.36.3
            # Browser: Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:122.0) Gecko/20100101 Firefox/122.0
            # Browser: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
            # Browser: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"}
            # include windows edge, chrome, firefox
            if "Mozilla/" in browser_name:
                return make_response(render_template('invalid.html'))
            else:
                return {"message": f"AuthenticationRootController successful. Browser: {browser_name}"}

        except Exception as e:
            logger.error("Error logging request details: %s", str(e))
            return {"SystemError": "An error happened during authentication. Please try later."}

class AuthenticationIdController(Resource):

    def get(self, user_id=None):

        try:

            if user_id:
                return {"message": "Authentication successful"}
            
            else:
                raise Exception("Testing exception")

        except Exception as e:
            logger.error("Error logging request details: %s", str(e))
            return {"SystemError": "An error happened during authentication. Please try later."}
#from src.services.urlPreviewService import urlPreviewService
from flask_restful import Resource, request

#url_preview_service = urlPreviewService.UrlPreviewService()


class UrlPreviewController(Resource):

    def get(self):
        json_payload = request.get_json()
        #return url_preview_service.getUrlPreviewHTML(url=json_payload['url'])
        return "test"

    def post(self):
        api_key = request.headers.get('api-key')
        #return url_preview_service.getUrlPreviewHTML(str(api_key))
        return "test"

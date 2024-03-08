from src.controllers.urlPreviewController import UrlPreviewController
from src.routes.urlPreview import url_preview_api


class UrlPreviewRouter:

    def __init__(self):
        url_preview_api.add_resource(UrlPreviewController, '/', endpoint='url-preview')

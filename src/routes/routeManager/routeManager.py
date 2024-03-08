from src.routes.helloWorld.helloWorldRouter import HelloWorldRouter
from src.routes.document.documentRouter import DocumentRouter
from src.routes.urlPreview.urlPreviewRouter import UrlPreviewRouter

class RouteManager:

    def __init__(self):
        self.helloWorldRouter = HelloWorldRouter()
        self.documentRouter = DocumentRouter()
        self.urlPreviewRouter = UrlPreviewRouter()

## 0.0.001

from src.routes.helloWorld.helloWorldRouter import HelloWorldRouter
from src.routes.document.documentRouter import DocumentRouter
from src.routes.urlPreview.urlPreviewRouter import UrlPreviewRouter
from src.routes.authentication.authenticationRouter import AuthenticationRouter

from logging import getLogger

logger = getLogger(__name__)

class RouteManager:

    def __init__(self):
        # this code is run once, during the start of the application.
        logger.info("RouteManager.__init__()")

        self.helloWorldRouter = HelloWorldRouter()
        self.documentRouter = DocumentRouter()
        self.urlPreviewRouter = UrlPreviewRouter()
        self.authenticationRouter = AuthenticationRouter()

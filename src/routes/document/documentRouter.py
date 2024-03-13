from src.controllers.documentController import DocumentController, DocumentAllController, DocumentAllIdsController
from src.routes.document import document_api_root #, document_api_id, document_api_all


class DocumentRouter:

    def __init__(self):
        document_api_root.add_resource(DocumentController, '/document', endpoint='document_root') # /document + JSON payload
        #document_api_id.add_resource(DocumentController, '/', endpoint='document_id')     # /document/<string:document_id>

        #document_api_all.add_resource(DocumentAllController, '/', endpoint='document_all')
        #document_api_all.add_resource(DocumentAllIdsController, '/ids', endpoint='document_all_ids')
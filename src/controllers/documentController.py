from src.services.documentService import documentService
from flask_restful import Resource, request as restful_request
from logging import getLogger

logger = getLogger(__name__)

document_service = documentService.DocumentService()

class DocumentController(Resource):

    def get(self, document_id=None):

        try:
            if document_id:
                #http://hostname/api/v1/document/5f3e3e3e3e3e3e3e3e3e3e3e
                logger.debug("getDocumentById() DocumentController.get() document_id: ", document_id)
                return document_service.getDocumentById(document_id=document_id)

            else:
                #http://hostname/api/v1/document
                logger.debug("DocumentController.get() document_service.getDocumentByJSON")
                return document_service.getDocumentByJson(restful_request)
                #return document_service.getDocumentAll()

        except Exception as e:
            logger.error("Error logging request details: %s", str(e))
        
        return "{ some: json }"

    def post(self):
        
        return document_service.insertDocument(restful_request)

    def delete(self):
        logger.info("deleteDocument() DocumentController.delete()")
        return document_service.deleteDocument(restful_request)


class DocumentAllController(Resource):

    def get(self):

        return document_service.getDocumentAll()


class DocumentAllIdsController(Resource):

    def get(self):

        return document_service.getDocumentAllIds()
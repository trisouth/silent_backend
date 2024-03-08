from src.services.documentService import documentService
from flask_restful import Resource, request
from logging import getLogger

logger = getLogger(__name__)

document_service = documentService.DocumentService()


class DocumentController(Resource):

    def get(self, document_id=None):

        if document_id:
            #http://hostname/api/v1/document/5f3e3e3e3e3e3e3e3e3e3e3e
            logger.info("getDocumentById() DocumentController.get() document_id: ", document_id)
            return document_service.getDocumentById(document_id=document_id)

        else:
            #http://hostname/api/v1/document
            logger.info("getDocumentByJson() DocumentController.get() document_id: ", document_id)
            return document_service.getDocumentByJson(request)
            #return document_service.getDocumentAll()

    def post(self):
        
        return document_service.insertDocument(request)

    def delete(self):
        logger.info("deleteDocument() DocumentController.delete()")
        return document_service.deleteDocument(request)


class DocumentAllController(Resource):

    def get(self):

        return document_service.getDocumentAll()


class DocumentAllIdsController(Resource):

    def get(self):

        return document_service.getDocumentAllIds()
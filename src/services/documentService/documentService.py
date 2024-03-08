import bson.json_util
from bson import ObjectId
from bson.errors import InvalidId
from flask import current_app, Response
import json
from logging import getLogger


from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo


logger = getLogger(__name__)

class DocumentService:

    def __init__(self):
        pass

    def getDocumentById(self, document_id):

        logger.info("getDocumentById document_id: " + document_id)
        if document_id:
            logger.info("getDocumentById document_id: " + document_id)
            return self.getDocument(document_id=document_id)

        else:
            return Response(json.dumps({'error': 'invalid object_id'}), status=404, mimetype='application/json')

    def getDocumentByJson(self, request):

        json_payload = request.get_json()
        if 'object_id' in json_payload:
            logger.info("getDocumentByJson document_id: " + str(json_payload['object_id']))
            
            return self.getDocument(json_payload['object_id'])

        else:
            return Response(json.dumps({'error4': 'invalid object_id'}), status=404, mimetype='application/json')
    
    def getDocument(self, document_id):

        db = g._database = PyMongo(current_app).db
        collection = db[current_app.config['MONGO_COLL']]

        try:
            # to test whether the given id is a valid ObjectId
            ObjectId(document_id)
            logger.info("After objectID document_id: " + str(document_id))

            if current_app:

                logger.info("After objectID document_id2: " + str(document_id))
  
                #document = current_app.config['MONGO_COLL'].find_one({"_id": ObjectId(document_id)})
                document = collection.find_one({"_id": ObjectId(document_id)})
                #document = db.users.find_one({"_id": ObjectId(document_id)})

            if document:
                # Convert ObjectId to string, so that the document can be serializable
                document['_id'] = str(document['_id'])

                return Response(bson.json_util.dumps(document), status=200, mimetype='application/json')

            else:
                # Return a 404 error if the document is not found
                return Response(json.dumps({"Database": "Document not found"}), status=404, mimetype='application/json')

        except (InvalidId, TypeError, ValueError) as e:
            message = json.dumps({'error2': f'Exception: {e}'})
            return Response(message, status=422, mimetype='application/json')

    def getDocumentAll(self):
        db = g._database = PyMongo(current_app).db
        collection = db[current_app.config['MONGO_COLL']]

        #documents = current_app.config['MONGO_COLL'].find({})
        documents = collection.find({})

        # Return the document IDs as JSON
        return Response(bson.json_util.dumps(documents), status=200, mimetype='application/json')


    def getDocumentAllIds(self):
        document_ids = [str(doc['_id']) for doc in current_app.config['MONGO_COLL'].find({}, {"_id": 1})]

        return Response(bson.json_util.dumps(document_ids), status=200, mimetype='application/json')

    def insertDocument(self, request):

        ###logger.info("insertDocument: " + str(request.get_json()))
        ####result = current_app.config['MONGO_COLL'].insert_one(request.get_json())
        ###result_data = {
        ###    #"_id": str(result.inserted_id)
        ###    "_id": str(54226)
        ###}
        ###return Response(json.dumps(result_data), status=200, mimetype='application/json')

        ### Above is the original code. Below is developed for prototyping.

        logger.info("insertDocument: " + str(request.get_json()))
        username = request.get_json()['username']

        try:
            db = g._database = PyMongo(current_app).db
            logger.info("db ready")
            collection = db[current_app.config['MONGO_COLL']]
            logger.info("collection ready")
            result_data = collection.find_one({ 'username': username })
            logger.info("result_data fetched")

            if result_data:
                logger.info("User found: " + str(result_data))
                result_data['_id'] = str(result_data['_id'])
                return Response(json.dumps(result_data), status=200, mimetype='application/json')
            else:
                logger.info("User not found")
                return Response(json.dumps({'error': 'User not found'}), status=404, mimetype='application/json')
        
        except Exception as e:
            message = json.dumps({'error': f'Exception: {e}'})
            logger.info("Exception: " + str(e))
            return Response(message, status=422, mimetype='application/json')
        


    def deleteDocument(self, request):

        json_payload = request.get_json()
        if 'object_id' in json_payload:

            document_id = json_payload['object_id']
            try:
                # to test whether the given id is a valid ObjectId
                ObjectId(document_id)

                # Delete the document by ID
                result = current_app.config['MONGO_COLL'].delete_one({"_id": ObjectId(document_id)})

                if result.deleted_count == 1:
                    # Return success message if the document is deleted
                    return Response(json.dumps({"message": "Document deleted"}), status=200, mimetype='application/json')
                else:
                    # Return a 404 error if the document is not found
                    return Response(json.dumps({"error": "Document not found"}), status=404, mimetype='application/json')

            except (InvalidId, TypeError, ValueError) as e:
                message = json.dumps({'error': f'Exception: {e}'})
                return Response(message, status=422, mimetype='application/json')

        else:
            return Response(json.dumps({'error': 'invalid object_id'}), status=404, mimetype='application/json')
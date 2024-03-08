from src.services.helloWorldService import helloWorldService
from flask_restful import Resource

hello_world_service = helloWorldService.HelloWorldService()


class HelloWorldGetMessage(Resource):
    def get(self):
        return hello_world_service.getMessage()
    def post(self):
        pass


class HelloWorldGetRandomMessage(Resource):
    def get(self):
        return hello_world_service.getMessage()
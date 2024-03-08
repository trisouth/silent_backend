from src.controllers.helloWorldController import HelloWorldGetMessage, HelloWorldGetRandomMessage
from src.routes.helloWorld import hello_world_api


class HelloWorldRouter:

    def __init__(self):
        hello_world_api.add_resource(HelloWorldGetMessage, '/', endpoint='hello_world')
        hello_world_api.add_resource(HelloWorldGetRandomMessage, '/random', endpoint='hello_world_random')
from flask import Flask
from app.views import API

class RESPUIT(Flask):
    
    def __init__(self, name):
        self.api = API(self)
        super().__init__(name)

    def routes(self):
        self.api.routes()

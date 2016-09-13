from flask_restful import Api

class API(Api):
    
    def routes(self):
        
        from app.views.hot_pepper import HotPepper
        self.add_resource(HotPepper, '/hot_pepper')

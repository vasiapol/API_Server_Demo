from flask_restful import Resource

# Welcome
# displays welcome message


class Welcome(Resource):
    def get(self):
        return 'Hello world, this is our simple REST API Server :)'

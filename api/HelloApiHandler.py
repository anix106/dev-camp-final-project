from flask_restful import Api, Resource, reqparse

class HelloApiHandler(Resource):
    def get(self):
        return {'hello': 'Alex 👋🏾'}


    def post(self):
        print("inside post")
        
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)
        
        args = parser.parse_args()
        print(args)

        request_type = args['type']
        request_json = args['message']

        return_status = request_type
        return_msg = request_json

        if return_msg:
            message = "Your message Requested: {}".format(return_msg)
        else:
            message = "No message was requested"
        
        final_ret = {"status": return_status, "message": message}
        
        return final_ret
from flask_restx import Namespace, Resource

api = Namespace('user')


# @api.route('/user/')
# class UserView(Resource):
#     def get(self):
#         """
#         Get user info.
#         """
#         req_json = request.json
#         print(req_json)
#         user = user_service.create(req_json)
#         return "", 201, {"location": f"/users/{user.id}"}

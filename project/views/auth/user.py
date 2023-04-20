from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.decorators import auth_required


api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    @auth_required
    def get(self):
        """
        Get user info.
        """
        user = user_service.get_user_by_mail(self)
        return user

    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    @auth_required
    def patch(self):
        """
        Patch user data.
        """
        req_json = request.json
        user = user_service.get_user_by_mail(self)
        user_service.update(req_json, user)
        return "", 204

@api.route('/password/')
class UserChangePassword(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    @auth_required
    def put(self):
        """
        Change user password.
        """
        req_json = request.json
        user = user_service.get_user_by_mail(self)
        user_service.change_pwd(req_json, user)
        return "", 204
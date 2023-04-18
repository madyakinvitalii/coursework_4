from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service
from project.container import auth_service

api = Namespace('auth')


@api.route('/register/')
class UserRegister(Resource):
    def post(self):
        """
        Register user.
        """
        req_json = request.json
        print(req_json)
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@api.route('/login/')
class AuthsTokens(Resource):
    def post(self):
        """
        Get tokens.
        """
        data = request.json
        print('data', data)
        email = data.get("email", None)
        password = data.get("password", None)
        print('email', email)
        print('password', password)
        if None in [email, password]:
            return "", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        """
        Regenerate tokens.
        """
        data = request.json
        refresh_token = data.get("refresh_token", None)

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201

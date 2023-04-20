import jwt
from flask import request, abort, current_app


def auth_required(func):
    def wrapper(mail):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            user = jwt.decode(token, key=current_app.config["SECRET_KEY"], algorithms=['HS256'])
            mail = user.get("email")
            print("мыло", mail)
        except Exception as e:
            print("JWT decode exception", e)
            abort(401)
        return func(mail)
    return wrapper

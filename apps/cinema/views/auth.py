from flask import request
from flask_restplus import Resource
from webargs import fields as flds
from werkzeug.security import check_password_hash, generate_password_hash

from apps.cinema import api
from apps.cinema.schema import param, validate_date
from apps.cinema.schema.parser import use_args
from apps.cinema.schema.user_schema import (
    login_schema,
    user_login_schema,
    user_request_fields,
    user_schema,
    user_schema_fields,
)
from apps.middlewares.auth import generate_token, is_admin, token_header
from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController

user_args = {
    "id": param(flds.Int(required=True)),
    "email": param(flds.Str()),
    "report": param(flds.Bool()),
    "name": param(flds.Str()),
    "ticket_startdate": param(flds.Str(validate=validate_date)),
    "ticket_enddate": param(flds.Str(validate=validate_date)),
    "total": param(flds.Float()),
}


@api.route("/auth", endpoint="user")
class UserRegistration(Resource):
    @api.marshal_with(user_schema_fields, envelope="user", skip_none=True)
    @api.expect(user_request_fields)
    def post(self):
        user = api.payload
        api.schema_model("User", {**user_schema}).validate(user)
        user["password"] = generate_password_hash(
            user["password"], method="sha256"
        )
        controller = UserController()
        if not controller.find_one(email=user.get("email")):
            user = controller.insert(user)
            return user, 201
        raise ValidationError(
            message="error",
            status_code=400,
            payload={"message": "User with email already exists"},
        )

    @api.marshal_with(user_schema_fields, envelope="user", skip_none=True)
    @api.doc(security="Authorisation")
    @token_header
    def get(self, **kwargs):
        return request.user._asdict(), 200


@api.route("/login", endpoint="login")
class LoginResource(Resource):
    @api.marshal_with(login_schema, envelope="user", skip_none=True)
    @api.expect(user_request_fields)
    def post(self):
        request_data = api.payload
        api.schema_model("User", {**user_login_schema}).validate(request_data)
        controller = UserController()
        user = controller.find_one(email=request_data.get("email"))
        if user and check_password_hash(
            user.password, request_data["password"]
        ):
            token = generate_token(user)
            return {"token": token, **user._asdict()}, 200
        raise ValidationError(
            message="error",
            status_code=401,
            payload={"message": "Invalid credentials"},
        )


@api.route("/users", endpoint="users")
class UserQueryAndReport(Resource):
    @api.marshal_with(user_schema_fields, envelope="user", skip_none=True)
    @token_header
    @is_admin
    @use_args(user_args)
    def get(self, params, **kwargs):
        controller = UserController()
        return controller.find(serialize=True, params=params, **kwargs), 200

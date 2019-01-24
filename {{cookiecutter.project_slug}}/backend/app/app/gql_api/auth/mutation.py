from datetime import timedelta

import graphene
from flask import abort
from flask_jwt_extended import create_access_token, get_current_user, jwt_required

from app.core.security import verify_password
from app.core import config
from app.gql_api.base import BaseMutation, default_model_resolver
from app.models.user import User as UserModel
from app.db.users import get_user
from app.gql_api.user.types import User


class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user = get_user(kwargs['email'])
        if user is None:
            no_user_msg = "No user found for {0}".format(kwargs['email'])
            abort(400, no_user_msg)
        if verify_password(kwargs['password'], user.password) is False:
            bad_pwd_msg = "Bad password for {0}".format(kwargs['email'])
            abort(400, bad_pwd_msg)
        token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            identity=kwargs['email'], expires_delta=token_expires)
        return Login(token=token, user=user)


class Logout(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info, **kwargs):
        # TODO: strategy for logging out? blacklist the token?
        return Logout(status="Logged out successfully.")


class Mutation(BaseMutation):
    login = Login.Field()
    logout = Logout.Field()

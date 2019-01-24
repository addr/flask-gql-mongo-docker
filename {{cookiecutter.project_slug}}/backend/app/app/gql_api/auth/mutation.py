import graphene

from app.core.security import verify_password
from app.gql_api.base import BaseMutation, default_model_resolver
from app.models.user import User as UserModel
from app.db.users import get_user
from app.gql_api.user.types import User
from .types import Payload


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
            raise Exception(no_user_msg)
        if verify_password(kwargs['password'], user.password) is False:
            bad_pwd_msg = "Bad password for {0}".format(kwargs['email'])
            raise Exception(bad_pwd_msg)
        token = user.get_auth_token()
        login_user(user)
        return Login(token=token, user=user)


class Logout(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info, **kwargs):
        logout_user()
        return Logout(status="Logged out successfully.")


class TokenAuth(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()

    def mutate(self, info, email, password):
        user = UserModel.objects.filter(email=email).first()

        if not user:
            raise Exception('User not found.')

        if not verify_password(password, user.password):
            raise Exception('Incorrect password.')

        token = create_access_token(identity=email)
        login_user(user)
        return TokenAuth(token=token)


class VerifyToken(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    payload = graphene.Field(Payload)

    @jwt_required
    def mutate(self, info, token):
        identity = get_jwt_identity()

        if not identity:
            payload = Payload()
        else:
            print(identity)
            payload = Payload(email=identity)

        return VerifyToken(payload=payload)


class Mutation(BaseMutation):
    login = Login.Field()
    logout = Logout.Field()

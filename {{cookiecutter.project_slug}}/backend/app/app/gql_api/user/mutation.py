# Import installed packages
import graphene
from flask import abort

# Import app code
from app.gql_api.base import BaseMutation, default_model_resolver
from .types import User
from app.models.user import User as UserModel
from app.db.users import get_user, create_user
from app.db.roles import create_or_get_role
from app.core.security import get_password_hash


class CreateUser(graphene.Mutation):
    # TODO: Add authentication to make sure the requesting user has permission
    # to create users (and if they can create users with the requested role)
    user = graphene.Field(User)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role_ids = graphene.List(graphene.ID)
        first_name = graphene.String()
        last_name = graphene.String()
        active = graphene.Boolean()

    Output = User

    def mutate(self, info, **kwargs):
        user = get_user(kwargs['email'])
        if user is not None:
            abort(400, "User already exists")
        role_ids = kwargs.get('role_ids', None)
        if role_ids is None:
            roles = [create_or_get_role("user")]
        else:
            roles = [
                default_model_resolver(self, info=info, id=id)
                for id in role_ids
            ]
        kwargs['roles'] = roles
        user = create_user(**kwargs)

        return user


class UpdateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        id = graphene.ID(required=True)
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        active = graphene.Boolean()
        role_ids = graphene.List(graphene.ID)

    Output = User

    def mutate(self, info, id, **kwargs):
        user = default_model_resolver(self, info=info, id=id)
        pw = kwargs.get('password', None)
        if pw is not None:
            kwargs['password'] = get_password_hash(pw)
        user.update(**kwargs)
        user.save()

        return user


class DeleteUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        id = graphene.ID(required=True)

    Output = User

    def mutate(self, info, id):
        user = default_model_resolver(self, info=info, id=id)
        user.delete()

        return user


class Mutation(BaseMutation):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

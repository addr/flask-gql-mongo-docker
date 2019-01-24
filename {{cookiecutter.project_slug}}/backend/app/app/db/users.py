# Import app code
from app.models.user import User
from app.db.roles import create_or_get_role
from app.core.security import get_password_hash


def get_user(email):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def create_user(email,
                password,
                roles,
                first_name=None,
                last_name=None,
                active=True):
    pw = get_password_hash(password)
    user = User(
        email=email,
        password=pw,
        roles=roles,
        first_name=first_name,
        last_name=last_name,
        active=active)
    user.save()
    return user


def create_or_get_user(email, password, is_superuser=False, **kwargs):
    user = get_user(email)
    roles = [create_or_get_role(name='user')]
    if is_superuser:
        roles.append(create_or_get_role(name='superuser'))
    if user is None:
        user = create_user(email, password, roles, **kwargs)
    return user

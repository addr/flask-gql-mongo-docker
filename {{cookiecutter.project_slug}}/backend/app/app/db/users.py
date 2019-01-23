# Import app code
from app.models.user import User
from app.db.roles import create_or_get_role


def get_user(email):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def create_or_get_user(email, password, is_superuser=False):
    user = get_user(email)
    roles = [create_or_get_role(name='user')]
    if is_superuser:
        roles.append(create_or_get_role(name='superuser'))
    if user is None:
        user = User(email=email, password=password, roles=roles)
        user.save()

    return user

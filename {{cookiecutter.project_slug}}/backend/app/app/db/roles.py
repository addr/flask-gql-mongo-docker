# Import app code
from app.models.role import Role


def get_role(name):
    try:
        return Role.objects.get(name=name)
    except Role.DoesNotExist:
        return None


def create_or_get_role(name):
    role = get_role(name)
    if role is None:
        role = Role(name=name)
        role.save()

    return role

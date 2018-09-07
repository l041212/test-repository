from apps.login.models import *

def getUserById(id):
    set = User.objects.filter(pk=id, isDelete=False)
    return set[0] if len(set) > 0 else None

def getUserByRole(role):
    set = User.objects.filter(role=role, isDelete=False)
    return set if len(set) > 0 else None
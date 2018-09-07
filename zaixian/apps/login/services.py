from apps.login.models import *
from apps.utils.commons import *

def getUserById(id):
    set = User.objects.filter(pk=id, isDelete=False)
    return set[0] if len(set) > 0 else None

def getUserByRole(role):
    set = User.objects.filter(role=role, isDelete=False)
    return set if len(set) > 0 else None

def saveUser(request, entity):
    entity = writeFlowInfoSimple(request, entity, User, User)
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False

def getUserByCodeAndPassword(code, password):
    users = User.objects.filter(code=code, password=password)
    return users
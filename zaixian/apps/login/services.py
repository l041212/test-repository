from apps.login.models import *
from apps.utils.commons import *
from functools import wraps

def getUserById(id):
    set = User.objects.filter(pk=id, isDelete=False)
    return set[0] if len(set) > 0 else None

def sessionUser():
    def method(funct):
        @wraps(funct)
        def wrapper(request,*args,**kwargs):
            user_id = request.session.get('user_id', None)
            user = getUserById(user_id) if isNotNull(user_id, 'str') else None
            return funct(request, sessionUser=user, *args, **kwargs)
        return wrapper
    return method

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
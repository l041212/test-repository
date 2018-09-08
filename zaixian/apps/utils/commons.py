from functools import wraps

def mirror(entity=None):
    def method(funct):
        @wraps(funct)
        def wrapper(request, *args, **kwargs):
            return funct(request, entity=lens(request, entity), *args, **kwargs)
        return wrapper
    return method

def lens(request, entity=None):
    if (entity != None):
        items = request.POST.items() if (request.method == 'POST') else request.GET.items()
        for key, value in items:
            value = value if value.strip() != '' else None
            entity.__setattr__(key, value)
    return entity

def rewrite(entity, type):
    if (entity != None and entity.id != None):
        item = type.objects.get(pk=entity.id)
        for key, value in entity.__dict__.items():
            item.__setattr__(key, value)
        return item
    return entity

def opposite(set):
    list = []
    for item in set:
        list.append(reverse(item))
    return list

def reverse(set):
    dict = {}
    for key in set.__dict__:
        dict[key] = str(set.__getattribute__(key))
    return dict

def writeFlowInfo(entity, type):
    if isNotNull(entity.id, 'str'):
        items = type.objects.filter(pk=entity.id)
        if len(items) > 0:
            entity.createUser = items[0].createUser
            entity.createTime = items[0].createTime
            entity.isDelete = items[0].isDelete
    return entity

def writeFlowInfoSimple(request, entity, userType, entityType):
    user = userType.objects.filter(pk=request.session['user_id'])[0]
    entity = writeFlowInfo(entity, entityType)
    entity.updateUser = user.id
    entity.createUser = entity.createUser if isNotNull(entity.createUser, 'str') else user.id
    return entity

def isNotNull(value, type):
    if type == 'str':
        return value != None and value != 'None' and str(value).strip() != ''
    return False

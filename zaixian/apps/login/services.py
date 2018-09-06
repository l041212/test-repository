from apps.login.models import *

def getUserById(id):
    set = User.objects.filter(pk=id)
    return set[0] if len(set) > 0 else None
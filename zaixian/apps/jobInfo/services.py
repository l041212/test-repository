from apps.utils.commons import *
from apps.login.models import *
from apps.jobInfo.models import *
from apps.jobInfo.services import *

def getJobInfoById(id):
    entity = None
    if isNotNull(id, 'str'):
        set = JobInfo.objects.filter(pk=id)
        if len(set) > 0:
            entity = reverse(set[0])
    return entity

def saveJobInfo(request, entity):
    user = User.objects.filter(pk=request.session['user_id'])[0]
    entity = writeFlowInfo(entity, JobInfo)
    entity.updateUser = user.id
    entity.createUser = entity.createUser if isNotNull(entity.createUser, 'str') else user.id
    entity.status = entity.status if isNotNull(entity.status, 'str') else '0'
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False


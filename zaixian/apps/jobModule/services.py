from apps.jobModule.models import *
from apps.jobInfo.models import *
from apps.login.models import *
from apps.utils.commons import *
from apps.jobInfo.services import *

def getJobModuleById(id):
    entity = None
    if isNotNull(id, 'str'):
        set = JobModule.objects.filter(pk=id)
        if len(set) > 0:
            entity = reverse(set[0])
    return entity

def saveJobModule(request, entity):
    jobInfo = JobInfo.objects.filter(pk=entity.jobInfo_id)[0]
    if hasattr(entity,'jobInfo_status') and isNotNull(entity.jobInfo_status, 'str'):
        if isNotNull(entity.jobInfo_id, 'str'):
            jobInfo.status = entity.jobInfo_status
    entity = writeFlowInfoSimple(request, entity, User, JobModule)
    entity.status = entity.status if isNotNull(entity.status, 'str') else '0'
    try:
        saveJobInfo(request, jobInfo)
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False

def getJobModuleByFilter(entity):
    items = JobModule.objects.filter(isDelete=False)
    if isNotNull(entity.name, 'str'):
        items = items.filter(name__contains=entity.name)
    items = items.order_by('-updateTime')
    for item in items:
        jobInfo = JobInfo.objects.filter(pk=item.jobInfo_id)[0]
        item.jobInfo_name = jobInfo.name
        item.jobInfo_status = jobInfo.status
    return items

def deleteModuleById(request, id):
    entity = JobModule.objects.filter(pk=id)[0]
    entity = writeFlowInfoSimple(request, entity, User, JobModule)
    entity.isDelete = True
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False
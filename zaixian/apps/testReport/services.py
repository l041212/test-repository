from apps.utils.commons import *
from apps.login.models import *
from apps.testReport.models import *

def getTestReportById(id):
    entity = None
    if isNotNull(id, 'str'):
        set = TestReport.objects.filter(pk=id)
        if len(set) > 0:
            entity = reverse(set[0])
    return entity

def saveTestReport(request, entity):
    entity = writeFlowInfoSimple(request, entity, User, TestReport)
    entity.status = entity.status if isNotNull(entity.status, 'str') else '0'
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False
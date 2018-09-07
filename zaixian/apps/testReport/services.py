from django.db import connection
import time
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

def saveTestReportByUnTester(request, jobInfo_id, user_id):
    entity = TestReport()
    entity.jobInfo = JobInfo.objects.get(pk=jobInfo_id)
    entity.user_id = user_id
    entity = writeFlowInfoSimple(request, entity, User, TestReport)
    entity.status = '0'
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False

def getTestReportByFilter(entity):
    cursor = connection.cursor()
    query = ""
    where = ""
    order_by = ""
    query += "select t.id,t.createTime,t.`match`,t.status,u.name as user_name,j.name as jobInfo_name "
    query += "from apps_TestReport t "
    query += "left join apps_JobInfo j "
    query += "on t.jobInfo_id = j.id "
    query += "left join apps_User u "
    query += "on t.user_id = u.id "
    where += "u.name like '%%%%%s%%%%' " % entity.user_name if hasattr(entity, 'user_name') and isNotNull(entity.user_name, 'str') else ""
    where += "and " if isNotNull(where, 'str') and hasattr(entity, 'jobInfo_name') and isNotNull(entity.jobInfo_name, 'str') else ""
    where += "j.name like '%%%%%s%%%%' " % entity.jobInfo_name if hasattr(entity, 'jobInfo_name') and isNotNull(entity.jobInfo_name, 'str') else ""
    where += "and " if isNotNull(where, 'str') and isNotNull(entity.status, 'str') else ""
    where += "t.status = %s " % entity.status if isNotNull(entity.status, 'str') else ""
    where += "and " if isNotNull(where, 'str') else ""
    where += "t.isDelete = '0' "
    where = "where " + where
    order_by += "t.updateTime desc "
    order_by = "order by " + order_by
    cursor.execute(query + where + order_by)
    items = cursor.fetchall()
    return items

def rewriteTestReportPageData(pageList):
    list = []
    for item in pageList:
        map = {}
        map['id'] = item[0]
        map['createTime'] = str(item[1])
        map['match'] = str(item[2])
        map['status'] = item[3]
        map['user_name'] = item[4]
        map['jobInfo_name'] = item[5]
        list.append(map)
    return list

def deleteTestReportById(request, id):
    entity = TestReport.objects.filter(pk=id)[0]
    entity = writeFlowInfoSimple(request, entity, User, TestReport)
    entity.isDelete = True
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False
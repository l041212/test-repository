from apps.utils.commons import *
from apps.login.models import *
from apps.jobInfo.models import *
from apps.jobInfo.services import *
from django.db import connection

def getJobInfoById(id):
    entity = None
    if isNotNull(id, 'str'):
        set = JobInfo.objects.filter(pk=id)
        if len(set) > 0:
            entity = reverse(set[0])
    return entity

def getJobInfoByFilter(entity):
    cursor = connection.cursor()
    query = ""
    where = ""
    order_by = ""
    query += "select t1.id,t1.name,t1.status,ifnull(t2.id_count,0),ifnull(t3.match_count,0),ifnull(t4.status_count,0) from "
    query += "(select id,name,status,updateTime,isDelete from apps_JobInfo where isDelete = '0') t1 "
    query += "left join "
    query += "(select jobInfo_id,count(jobInfo_id) as id_count "
    query += "from apps_TestReport where isDelete = '0' group by jobInfo_id) t2 "
    query += "on t1.id = t2.jobInfo_id "
    query += "left join "
    query += "(select jobInfo_id,count(jobInfo_id) as match_count "
    query += "from apps_TestReport where `match` > 50 and isDelete = '0' group by jobInfo_id) t3 "
    query += "on t1.id = t3.jobInfo_id "
    query += "left join "
    query += "(select jobInfo_id,count(jobInfo_id) as status_count "
    query += "from apps_TestReport where status = 0 and isDelete = '0' group by jobInfo_id) t4 "
    query += "on t1.id = t4.jobInfo_id "
    where += "t1.name like '%%%%%s%%%%' " % entity.name if isNotNull(entity.name, 'str') else ""
    where += "and " if isNotNull(where, 'str') and isNotNull(entity.status, 'str') else ""
    where += "t1.status = %s " % entity.status if isNotNull(entity.status, 'str') else ""
    where += "and " if isNotNull(where, 'str') else ""
    where += "t1.isDelete = '0' "
    where = "where "+where
    order_by += "t1.updateTime desc "
    order_by = "order by "+order_by
    cursor.execute(query+where+order_by)
    items = cursor.fetchall()
    return items

def rewriteJobInfoPageData(pageList):
    list = []
    for item in pageList:
        map = {}
        map['id'] = item[0]
        map['name'] = item[1]
        map['status'] = item[2]
        map['id_count'] = item[3]
        map['match_count'] = item[4]
        map['status_count'] = item[5]
        list.append(map)
    return list

def saveJobInfo(request, entity):
    entity = writeFlowInfoSimple(request, entity, User, JobInfo)
    entity.status = entity.status if isNotNull(entity.status, 'str') else '0'
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False

def deleteJobInfoById(request, id):
    entity = JobInfo.objects.filter(pk=id)[0]
    entity = writeFlowInfoSimple(request, entity, User, JobInfo)
    entity.isDelete = True
    try:
        entity.save()
        return True
    except Exception as e:
        print(e)
        return False

def getJobInfoByUnModule():
    return JobInfo.objects.filter(isDelete=False, status='0')
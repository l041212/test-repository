from django.shortcuts import render
from django.http import HttpResponse
import json
from apps.base.models import *
from apps.jobInfo.services import *
from apps.login.services import *

@sessionUser()
def table(request, action, id, sessionUser):
    context = {
        'action': action,
        'id': id if isNotNull(id, 'str') else None,
        'jobInfo': getJobInfoById(id),
        'sessionUser': sessionUser,
    }
    return render(request, 'jobInfo_table.html', context)

@sessionUser()
def list(request, page_limit, sessionUser):
    context = {
        'page_limit': page_limit if isNotNull(page_limit, 'str') else '10',
        'page_number': '1',
        'sessionUser': sessionUser,
    }
    return render(request, 'jobInfo_list.html', context)

@mirror(JobInfo())
def listData(request, entity, page_limit, page_number):
    items = getJobInfoByFilter(entity)
    page = SimplePage().writeSimplePage(items, page_limit, page_number)
    page.page_object_list = json.dumps(rewriteJobInfoPageData(page.page_object_list))
    return HttpResponse(json.dumps(reverse(page)), content_type='application/json')

@mirror(JobInfo())
def save(request, entity):
    flag = saveJobInfo(request, entity)
    return HttpResponse(flag)

def delete(request):
    flag = True
    for id in request.POST.getlist("ids[]", []):
        flag &= deleteJobInfoById(request, id)
    return HttpResponse(flag)

def unModule(request):
    items = getJobInfoByUnModule()
    return HttpResponse(json.dumps(opposite(items)), content_type='application/json')

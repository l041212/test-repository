from django.shortcuts import render
from django.http import HttpResponse
import json
from apps.base.models import *
from apps.jobInfo.services import *

def table(request, action, id):
    user = User.objects.all()[0]
    request.session['user_id'] = user.id
    context = {
        'action': action,
        'id': id if isNotNull(id, 'str') else None,
        'jobInfo': getJobInfoById(id),
    }
    return render(request, 'jobInfo_table.html', context)

def list(request, page_limit):
    context = {
        'page_limit': page_limit if isNotNull(page_limit, 'str') else '25',
        'page_number': '1',
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

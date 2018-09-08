from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from apps.jobModule.models import *
from apps.login.models import *
from apps.utils.commons import *
from apps.jobInfo.services import getJobInfoById
from apps.jobModule.services import *
from apps.login.services import *
import json


# Create your views here.


def edit(request, jobInfo_id, id):
    #user = User.objects.all()[0]
    #request.session['user_id'] = user.id
    context = {
        'jobInfo_id': jobInfo_id,
        'id': id if isNotNull(id, 'str') else '',
        'jobInfo_name': getJobInfoById(jobInfo_id)['name'],
        'jobInfo_status': getJobInfoById(jobInfo_id)['status'],
    }
    return render(request, 'test1.html', context)

def lol(request):
    if request.method == "POST":
        JobModule.objects.create(name=request.POST['name'],text=request.POST['text'],attachment=request.POST['attachment'])
    return render_to_response('test1.html',locals())

def list(request):
    people_list = JobModule.objects.all()
    return render(request,'show.html',{"people_list":people_list})

def yaya(request):
    return render(request,'show.html')

@sessionUser()
def table(request, action, id, sessionUser):
    jobModule = getJobModuleById(id)
    jobInfo = getJobInfoById(jobModule['jobInfo_id']) if jobModule != None and isNotNull(jobModule['jobInfo_id'], 'str') else None
    context = {
        'action': action,
        'id': id if isNotNull(id, 'str') else None,
        'jobModule': jobModule,
        'jobInfo':  jobInfo,
        'sessionUser': sessionUser,
    }
    return render(request, 'jobModule_table.html', context)

@mirror(JobModule())
def save(request, entity):
    flag = saveJobModule(request, entity)
    return HttpResponse(flag)

@sessionUser()
def list(request, page_limit, sessionUser):
    context = {
        'page_limit': page_limit if isNotNull(page_limit, 'str') else '10',
        'page_number': '1',
        'sessionUser': sessionUser,
    }
    return render(request, 'jobModule_list.html', context)

@mirror(JobInfo())
def listData(request, entity, page_limit, page_number):
    items = opposite(getJobModuleByFilter(entity))
    page = SimplePage().writeSimplePage(items, page_limit, page_number)
    page.page_object_list = json.dumps(page.page_object_list)
    return HttpResponse(json.dumps(reverse(page)), content_type='application/json')

def delete(request):
    flag = True
    for id in request.POST.getlist("ids[]", []):
        flag &= deleteModuleById(request, id)
    return HttpResponse(flag)



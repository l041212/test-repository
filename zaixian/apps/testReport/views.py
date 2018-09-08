from django.shortcuts import render
from django.http import HttpResponse
import json
from apps.login.services import *
from apps.jobInfo.services import *
from apps.testReport.services import *
from apps.base.models import *


def test(request):
    return render(request,'test.html')


def test_choice(request):
    return render(request, 'test_choice.html')


def test_new(request):
    return render(request,'test_new.html')

@sessionUser()
def edit(request, action, id, sessionUser):
    testReport = getTestReportById(id)
    context = {
        'action': action,
        'id': id if isNotNull(id, 'str') else None,
        'testReport': testReport,
        'jobInfo': getJobInfoById(testReport['jobInfo_id']) if isNotNull(testReport['jobInfo_id'], 'str') else None,
        'user': getUserById(testReport['user_id']) if isNotNull(testReport['user_id'], 'str') else None,
        'sessionUser': sessionUser,
    }
    return render(request, 'testReport_edit.html', context)

@sessionUser()
def list(request, page_limit, sessionUser):
    context = {
        'page_limit': page_limit if isNotNull(page_limit, 'str') else '10',
        'page_number': '1',
        'sessionUser': sessionUser,
    }
    return render(request, 'testReport_list.html', context)

@sessionUser()
def list_invite(request, page_limit, sessionUser):
    context = {
        'page_limit': page_limit if isNotNull(page_limit, 'str') else '10',
        'page_number': '1',
        'sessionUser': sessionUser,
    }
    return render(request, 'testReport_list_invite.html', context)

@mirror(TestReport())
def save(request, entity):
    flag = saveTestReport(request, entity)
    return HttpResponse(flag)

def save_invite(request):
    flag = True
    jobInfo_id = request.POST["jobInfo_id"]
    for user_id in request.POST.getlist("users_id[]", []):
        flag &= saveTestReportByUnTester(request, jobInfo_id, user_id)
    return HttpResponse(flag)

@mirror(TestReport())
def listData(request, entity, page_limit, page_number):
    items = getTestReportByFilter(entity)
    page = SimplePage().writeSimplePage(items, page_limit, page_number)
    page.page_object_list = json.dumps(rewriteTestReportPageData(page.page_object_list))
    return HttpResponse(json.dumps(reverse(page)), content_type='application/json')

def delete(request):
    flag = True
    for id in request.POST.getlist("ids[]", []):
        flag &= deleteTestReportById(request, id)
    return HttpResponse(flag)

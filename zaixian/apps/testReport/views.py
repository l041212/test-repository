from django.shortcuts import render
from django.http import HttpResponse
from apps.login.services import *
from apps.jobInfo.services import *
from apps.testReport.services import *


def test(request):
    return render(request,'test.html')


def test_choice(request):
    return render(request, 'test_choice.html')


def test_new(request):
    return render(request,'test_new.html')

def edit(request, action, id):
    user = User.objects.all()[0]
    request.session['user_id'] = user.id
    testReport = getTestReportById(id)
    context = {
        'action': action,
        'id': id if isNotNull(id, 'str') else None,
        'testReport': testReport,
        'jobInfo': getJobInfoById(testReport['jobInfo_id']) if isNotNull(testReport['jobInfo_id'], 'str') else None,
        'user': getUserById(testReport['user_id']) if isNotNull(testReport['user_id'], 'str') else None,
    }
    return render(request, 'testReport_edit.html', context)

@mirror(TestReport())
def save(request, entity):
    flag = saveTestReport(request, entity)
    return HttpResponse(flag)

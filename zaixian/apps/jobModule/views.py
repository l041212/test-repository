from django.shortcuts import render
from django.http import HttpResponse
from apps.jobModule.models import *
from apps.login.models import *
from apps.utils.commons import *
from apps.jobInfo.services import getJobInfoById

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

@mirror(JobModule())
def save(request, entity):
    print(entity.id)
    print(entity.jobInfo_id)
    print(entity.jobInfo_status)
    print(entity.name)
    print(entity.text)
    return HttpResponse("success")


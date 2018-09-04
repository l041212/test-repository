from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse
from apps.jobInfo.services import *

# Create your views here.

def table(request, action, id):
    user = User.objects.all()[0]
    request.session['user_id'] = user.id
    context = {
        'action': action,
        'id': id if isNotNull(id, 'str') else None,
        'jobInfo': getJobInfoById(id),
    }
    return render(request, 'jobInfo_table.html', context)

def list(request):
    return render(request, 'jobInfo_list.html')

@mirror(JobInfo())
def save(request, entity):
    flag = saveJobInfo(request, entity)
    return HttpResponse(flag)
>>>>>>> 0f66454e5bd17ae4133c11fc769183559dbd1b8d

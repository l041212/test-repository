from django.shortcuts import render
from django.http import HttpResponse
import json
from apps.utils.commons import *
from apps.userinfo.models import User

# Create your views here.

@mirror(User())
def indexInit(request, entity = None):
    if entity.name == None:
        return render(request, 'login_info.html')
    return HttpResponse(json.dumps(reverse(entity)), content_type='application/json')

def frameInit(request):
    return render(request, 'login_frame.html')
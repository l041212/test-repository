from django.shortcuts import render
from django.http import HttpResponse
import json
from apps.utils.commons import *
from apps.userinfo.models import User

# Create your views here.

def init(request, id = None):
    return render(request, 'userinfo_info.html')

@mirror(User())
def save(request, entity = None, id = None):
    entity.save()
    return HttpResponse(json.dumps(reverse(entity)), content_type='application/json')
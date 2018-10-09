from django.http import HttpResponse
import json
from apps.utils.commons import *
from apps.library.models import *

# Create your views here.

def authorAllList(request):
    context = Author.objects.all()
    return HttpResponse(json.dumps(opposite(context)), content_type='application/json')
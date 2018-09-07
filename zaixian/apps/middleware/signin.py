import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from apps.utils.commons import *

class loginMiddleWare(MiddlewareMixin):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if(re.search(r'^/login', request.path) == None):
            print("user_id"+":"+str(request.session["user_id"]))
            if(not isNotNull(request.session["user_id"], 'str')):
                return HttpResponseRedirect("/login/info/")
        return None
import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from apps.utils.commons import *

class loginMiddleWare(MiddlewareMixin):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if(re.search(r'^/login', request.path) == None):
            request.session.set_expiry(24*3600)
            if(not isNotNull(request.session.get("user_id", None), 'str')):
                return HttpResponseRedirect("/login/info/")
        else:
            request.session.flush()
        return None
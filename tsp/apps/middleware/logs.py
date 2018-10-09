from django.utils.deprecation import MiddlewareMixin

class LogsMiddleWare(MiddlewareMixin):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        meta = request.META
        for key, value in meta.items():
            print(key + ':' + str(value))
        return None

    def process_response(self, request, response):
        return response
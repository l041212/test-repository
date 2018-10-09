from django.contrib import admin
from apps.library.models import *

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publisher)
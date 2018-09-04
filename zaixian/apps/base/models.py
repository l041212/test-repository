from django.db import models
from django.core.paginator import Paginator
import django.utils.timezone as timezone

# Create your models here.
class Base(models.Model):

    class Meta(object):
        abstract = True

    createUser = models.CharField(max_length=32, null=True, default=None)
    updateUser = models.CharField(max_length=32, null=True, default=None)
    createTime = models.DateTimeField(null=True, default=timezone.now)
    updateTime = models.DateTimeField(null=True, auto_now=True)
    status = models.CharField(max_length=16, null=True, default=None)
    isDelete = models.BooleanField(null=True, default=False)

class SimplePage(object):

    page_limit = None
    page_count = None
    page_number = None
    page_object_list = None
    page_previous = None
    page_previous_p = None
    page_next = None
    page_next_n = None

    def writeSimplePage(self, set, page_limit, page_number):
        self.page_limit = int(page_limit)
        self.page_number = int(page_number)
        paginator = Paginator(set, self .page_limit)
        self.page_number = int(page_number) if paginator.num_pages >= int(page_number) else paginator.num_pages
        page = paginator.page(self.page_number)
        self.page_count = page.paginator.count
        self.page_object_list = page.object_list
        self.page_previous = page.has_previous()
        self.page_previous_p = paginator.page(self.page_number-1).has_previous() if self.page_previous else False
        self.page_next = page.has_next()
        self.page_next_n = paginator.page(self.page_number+1).has_next() if self.page_next else False
        return self

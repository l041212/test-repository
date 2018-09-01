from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Base(models.Model):

    def Meta(object):
        abstract = True

    createUser = models.CharField(max_length=32, null=True)
    updateUser = models.CharField(max_length=32, null=True)
    createTime = models.DateTimeField(auto_now=True)
    updateTime = models.DateTimeField(null=True, default=timezone)
    status = models.CharField(max_length=16, null=True, default=None)
    isDelete = models.BooleanField(null=True, default=False)
from django.db import models
from apps.base.models import Base

# Create your models here.
class JobInfo(Base):

    class Meta(object):
        db_table = 'apps_JobInfo'

    #职业名称
    name = models.CharField(max_length=32, null=True, default=None)
    #职业属性
    property = models.CharField(max_length=32, null=True, default=None)
    #职业等级
    rank = models.CharField(max_length=32, null=True, default=None)
    #职业描述
    description = models.CharField(max_length=128, null=True, default=None)

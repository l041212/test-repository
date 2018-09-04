from django.db import models
from apps.base.models import Base
from apps.jobInfo.models import JobInfo

# Create your models here.
class JobRequirement(Base):

    class Meta(object):
        db_table = 'apps_JobRequirement'

    #教育
    education = models.CharField(max_length=20, null=True, default=None)
    #经验
    experience = models.CharField(max_length=256, null=True, default=None)
    #资历
    passTime = models.CharField(max_length=32, null=True, default=None)
    #证书
    certificate = models.CharField(max_length=128, null=True, default=None)
    #专业
    major = models.CharField(max_length=64, null=True, default=None)
    #技能
    skill = models.CharField(max_length=128, null=True, default=None)
    #职业信息ForeignKey
    jobInfo = models.ForeignKey(JobInfo, on_delete=models.CASCADE)


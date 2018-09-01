from django.db import models
from apps.base.models import Base

# Create your models here.
class JobRequirement(Base):
    education=models.CharField(max_length=20, null=True, default=None)
    experience=models.CharField(max_length=256, null=True, default=None)
    passtime=models.CharField(max_length=32, null=True, default=None)
    certificate=models.CharField(max_length=128, null=True, default=None)
    major=models.CharField(max_length=64, null=True, default=None)
    skill=models.CharField(max_length=128, null=True, default=None)
    #jobInfos=models.ForeignKey(JobInfo)


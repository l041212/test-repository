from django.db import models

# Create your models here.
class JobModule(models.Model):
        #模板名称
        name = models.CharField(max_length=32,null=True,default=False)
        #job表的外键
        job_id = models.CharField(max_length=20,null=True)
        #文本
        text = models.CharField(max_length=1024,null=True)
        #附件
        attachment = models.CharField(null=True,default=False,max_length=128)
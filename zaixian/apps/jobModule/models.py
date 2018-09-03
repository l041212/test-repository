from django.db import models

# Create your models here.
class JobModule(models.Model):

        class Meta(object):
                db_table = 'apps_JobModule'

        #模板名称
        name = models.CharField(max_length=32, null=True, default=False)
        #模板文本
        text = models.CharField(max_length=1024, null=True, default=False)
        #模板附件
        attachment = models.FileField(upload_to='media/attachment', null=True, default=None)
        #职业信息ID
        jobInfo_id = models.CharField(max_length=20, null=True, default=False)
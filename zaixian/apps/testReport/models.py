from django.db import models
from apps.base.models import Base
from apps.jobInfo.models import JobInfo

# Create your models here.
class TestReport(Base):

    class Meta(object):
        db_table = 'apps_TestReport'

    #报告名称
    name = models.CharField(max_length=32, null=True, default=None)
    #匹配度
    match = models.IntegerField(null=True, default=None)
    match = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.00)
    #报告文本
    text = models.CharField(max_length=1024, null=True, default=None)
    #报告附件
    attachment = models.FileField(upload_to='media/attachment', null=True, default=None)
    #用户ID
    user_id = models.IntegerField(null=True, default=None)
    # 职业信息ForeignKey
    jobInfo = models.ForeignKey(JobInfo, on_delete=models.CASCADE)

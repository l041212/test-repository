from django.db import models
from apps.base.models import Base

# Create your models here.
class User(Base):
    # id = models.AutoField(auto_created=True, primary_key=True, serialize=, verbose_name='ID'),
    #用户名称
    name = models.CharField(max_length=32, null=True, default=None)
    #帐号名称
    code = models.CharField(max_length=32, null=True, default=None)
    #用户角色
    role = models.CharField(max_length=16,null=True, default=None)
    #用户邮箱
    email = models.CharField(max_length=64, null=True, default=None)
    #用户密码
    password=models.CharField(max_length=100,null=True)

    class Meta(object):
        db_table = 'apps_User'
    # def create(self,email,passwd):
    #     self.email=email
    #     self.passwd=passwd
    #     self.save()
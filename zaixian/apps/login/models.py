from django.db import models
from apps.base.models import Base

# Create your models here.
class User(Base):

    class Meta(object):
        db_table = 'apps_User'

    # id = models.AutoField(auto_created=True, primary_key=True, serialize=, verbose_name='ID'),
    #用户名称
    name = models.CharField(max_length=32, null=True, default=None)
    #帐号名称
    code = models.CharField(max_length=32, null=True, default=None)
    #用户角色
    role = models.CharField(max_length=16,null=True, default=None)
    #用户邮箱
    email = models.CharField(max_length=64, null=True, default=None)
#   id int(20) primary key,
#   name varchar(32) default null comment '名称',
#   code varchar(32) default null comment '帐号名称',
#   role varchar(16) default null comment '角色权限',    --['tester','admin','hr']
#   email varchar(64) default null comment '邮箱地址',
#   status int(2) default null,       --[0,1,2]
#   isDelete int(2) default false
# )
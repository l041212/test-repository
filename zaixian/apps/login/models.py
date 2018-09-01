from django.db import models
from apps.base.models import Base

# Create your models here.
class User(Base):
    # id = models.AutoField(auto_created=True, primary_key=True, serialize=, verbose_name='ID'),
    name= models.CharField(max_length=32, null=True),
    code=models.CharField(max_length=32,null=True),
    role=models.CharField(max_length=16,null=True),
    email=models.CharField(max_length=64,null=True)
#   id int(20) primary key,
#   name varchar(32) default null comment '名称',
#   code varchar(32) default null comment '帐号名称',
#   role varchar(16) default null comment '角色权限',    --['tester','admin','hr']
#   email varchar(64) default null comment '邮箱地址',
#   status int(2) default null,       --[0,1,2]
#   isDelete int(2) default false
# )
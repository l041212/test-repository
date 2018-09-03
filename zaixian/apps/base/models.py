from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Base(models.Model):

    class Meta(object):
        abstract = True

    createUser = models.CharField(max_length=32, null=True, default=None)
    updateUser = models.CharField(max_length=32, null=True, default=None)
<<<<<<< Updated upstream
    createTime = models.DateTimeField(auto_now=True)
=======
    createTime = models.DateTimeField(null=True, auto_now=True)
>>>>>>> Stashed changes
    updateTime = models.DateTimeField(null=True, default=timezone.now)
    status = models.CharField(max_length=16, null=True, default=None)
    isDelete = models.BooleanField(null=True, default=False)
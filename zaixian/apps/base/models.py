from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Base(models.Model):

    def Meta(object):
        abstract = True

    createUser = models.CharField(max_length=32, null=True, default=None)
    updateUser = models.CharField(max_length=32, null=True, default=None)
    createTime = models.DateTimeField(auto_now=True)
<<<<<<< Updated upstream
    updateTime = models.DateTimeField(null=True, default=timezone.now)
=======
    updateTime = models.DateTimeField(null=True, default=timezone.now())
>>>>>>> Stashed changes
    status = models.CharField(max_length=16, null=True, default=None)
    isDelete = models.BooleanField(null=True, defaultl=False)
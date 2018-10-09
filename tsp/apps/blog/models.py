from django.db import models
import django.utils.timezone as timezone
from apps.library.models import Author

# Create your models here.

class Catalogue(models.Model):

    title = models.CharField(max_length=64, null=True)
    context = models.CharField(max_length=1024, null=True)
    createTime = models.DateTimeField(null=True, default=timezone.now)
    updateTime = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, default=None)
    isDelete = models.BooleanField(max_length=2, default=False)
    updateTime_from = None
    updateTime_to = None

class Category(models.Model):

    label = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=256, null=True)
    isDelete = models.BooleanField(max_length=2, default=False)

class Comment(models.Model):
    title = models.CharField(max_length=64, null=True)
    context = models.CharField(max_length=1024, null=True)
    createTime = models.DateTimeField(null=True, default=timezone.now)
    updateTime = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, default=None)
    isDelete = models.BooleanField(max_length=2, default=False)


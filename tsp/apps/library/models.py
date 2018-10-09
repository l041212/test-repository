from django.db import models

# Create your models here.

class Person(models.Model):

    class Meta(object):
        abstract = True
    SEX_CHOICES = (('m','male'),('f','female'),)
    name = models.CharField(max_length=32, null=True)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, null=True)
    age = models.IntegerField(null=True)
    isDelete = models.BooleanField(max_length=2, default=False)

class Author(Person):

    '''
    class Meta(object):
        db_table='author'
    '''
    penName = models.CharField(max_length=32, null=True)
    email = models.EmailField(max_length=64, null=True)
    authorDetail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, default=None)

class AuthorDetail(models.Model):

    location = models.CharField(max_length=64, null=True)
    favor = models.CharField(max_length=64, null=True)
    hate = models.CharField(max_length=64, null=True)
    isDelete = models.BooleanField(max_length=2, default=False)

class Book(models.Model):

    '''
    class Meta(object):
        db_table='book'
    '''

    name = models.CharField(max_length=32, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = models.ImageField(upload_to='media/', null=True)
    publishDate = models.DateField(null=True)
    publisher = models.ManyToManyField(to='Publisher')
    description = models.CharField(max_length=256, null=True)
    isDelete = models.BooleanField(max_length=2, default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)

class Publisher(models.Model):

    name=models.CharField(max_length=64, null=True)
    address=models.CharField(max_length=128, null=True)
    owner=models.CharField(max_length=32, null=True)
    isDelete=models.BooleanField(max_length=2, default=False)

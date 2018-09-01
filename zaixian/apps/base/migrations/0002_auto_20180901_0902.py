# Generated by Django 2.1 on 2018-09-01 09:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='createUser',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='base',
            name='updateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 9, 2, 38, 534013, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='base',
            name='updateUser',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
    ]

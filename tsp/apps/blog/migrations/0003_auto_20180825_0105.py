# Generated by Django 2.1 on 2018-08-25 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180824_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updateTime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]

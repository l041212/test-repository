# Generated by Django 2.1 on 2018-09-03 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createUser', models.CharField(default=None, max_length=32, null=True)),
                ('updateUser', models.CharField(default=None, max_length=32, null=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('updateTime', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(default=None, max_length=16, null=True)),
                ('isDelete', models.BooleanField(default=False, null=True)),
                ('name', models.CharField(default=None, max_length=32, null=True)),
                ('property', models.CharField(default=None, max_length=32, null=True)),
                ('rank', models.CharField(default=None, max_length=32, null=True)),
                ('description', models.CharField(default=None, max_length=128, null=True)),
            ],
            options={
                'db_table': 'apps_JobInfo',
            },
        ),
    ]

# Generated by Django 2.1 on 2018-09-01 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createUser', models.CharField(default=None, max_length=32, null=True)),
                ('updateUser', models.CharField(default=None, max_length=32, null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(default=None, max_length=16, null=True)),
                ('isDelete', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
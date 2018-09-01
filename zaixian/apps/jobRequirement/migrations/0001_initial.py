# Generated by Django 2.1 on 2018-09-01 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_auto_20180901_0858'),
        ('jobInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequirement',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Base')),
                ('education', models.CharField(default=None, max_length=20, null=True)),
                ('experience', models.CharField(default=None, max_length=256, null=True)),
                ('passTime', models.CharField(default=None, max_length=32, null=True)),
                ('certificate', models.CharField(default=None, max_length=128, null=True)),
                ('major', models.CharField(default=None, max_length=64, null=True)),
                ('skill', models.CharField(default=None, max_length=128, null=True)),
                ('jobInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobInfo.JobInfo')),
            ],
            bases=('base.base',),
        ),
    ]

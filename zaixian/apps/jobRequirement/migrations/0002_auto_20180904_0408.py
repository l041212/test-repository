# Generated by Django 2.1 on 2018-09-04 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobRequirement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequirement',
            name='jobInfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobInfo.JobInfo'),
        ),
    ]

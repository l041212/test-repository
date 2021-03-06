# Generated by Django 2.1 on 2018-09-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=32, null=True)),
                ('text', models.CharField(default=False, max_length=1024, null=True)),
                ('attachment', models.FileField(default=None, null=True, upload_to='media/attachment')),
                ('jobInfo_id', models.CharField(default=False, max_length=20, null=True)),
            ],
            options={
                'db_table': 'apps_JobModule',
            },
        ),
    ]

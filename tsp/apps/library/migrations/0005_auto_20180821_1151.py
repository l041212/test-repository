# Generated by Django 2.1 on 2018-08-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20180821_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='penName',
            field=models.CharField(max_length=32, null=True),
        ),
    ]

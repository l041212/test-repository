# Generated by Django 2.1 on 2018-08-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180825_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='isDelete',
            field=models.BooleanField(default=False, max_length=2),
        ),
    ]

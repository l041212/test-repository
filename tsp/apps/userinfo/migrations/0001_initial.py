# Generated by Django 2.1 on 2018-08-18 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('sex', models.CharField(max_length=4, null=True)),
                ('company', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
# Generated by Django 2.1 on 2021-04-20 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20210420_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='email',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='last_name',
        ),
    ]

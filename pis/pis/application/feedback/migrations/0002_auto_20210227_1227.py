# Generated by Django 2.1 on 2021-02-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='First_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Last_name',
            field=models.CharField(max_length=30, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Mobile',
            field=models.CharField(max_length=10, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Subject',
            field=models.CharField(max_length=30, verbose_name='Subject'),
        ),
    ]

# Generated by Django 2.1 on 2021-02-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hod', '0002_auto_20210226_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod',
            name='Exp',
            field=models.CharField(max_length=15, verbose_name='Experience'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='qua',
            field=models.CharField(max_length=30, verbose_name='Qualification'),
        ),
    ]

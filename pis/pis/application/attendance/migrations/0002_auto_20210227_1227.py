# Generated by Django 2.1 on 2021-02-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='lec_name',
            field=models.CharField(max_length=30, verbose_name='Lec_name'),
        ),
    ]

# Generated by Django 2.1 on 2021-02-27 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20210227_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'verbose_name': 'Assignment'},
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='ass_data',
            new_name='ass_date',
        ),
    ]

# Generated by Django 2.1 on 2021-04-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('departments_info', models.TextField(default='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]

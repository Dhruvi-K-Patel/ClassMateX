# Generated by Django 2.1 on 2021-02-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_name', models.CharField(max_length=30)),
                ('Branch_code', models.CharField(max_length=30)),
            ],
        ),
    ]

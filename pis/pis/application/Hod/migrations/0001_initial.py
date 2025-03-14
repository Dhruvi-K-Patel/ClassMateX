# Generated by Django 2.1 on 2021-02-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Id')),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('Exp', models.CharField(max_length=15)),
                ('qua', models.CharField(max_length=30)),
                ('dep', models.CharField(max_length=15)),
                ('Mobileno', models.CharField(max_length=10, verbose_name='Mobile Number')),
                ('DoB', models.DateField()),
            ],
        ),
    ]

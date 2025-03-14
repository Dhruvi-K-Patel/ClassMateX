# Generated by Django 2.1 on 2021-02-26 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_name', models.CharField(max_length=30)),
                ('Sub_code', models.IntegerField()),
                ('Day', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('Time', models.TimeField()),
                ('F_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty')),
            ],
        ),
    ]

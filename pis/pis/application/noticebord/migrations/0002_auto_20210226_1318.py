# Generated by Django 2.1 on 2021-02-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticebord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='Type',
            field=models.CharField(choices=[('E', 'Educational'), ('S', 'Seminar'), ('W', 'Workshop'), ('C', 'Curriculum Activity'), ('A', 'Admission process'), ('E', 'Exam'), ('R', 'Result')], max_length=1),
        ),
    ]

# Generated by Django 2.1 on 2021-03-01 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch', verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='result',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='Stuadent'),
        ),
        migrations.AlterField(
            model_name='result',
            name='ex_date',
            field=models.DateField(verbose_name='Exam Date'),
        ),
        migrations.AlterField(
            model_name='result',
            name='o_mark',
            field=models.IntegerField(verbose_name='Obtained Mark '),
        ),
        migrations.AlterField(
            model_name='result',
            name='total_mark',
            field=models.IntegerField(verbose_name='Total Mark'),
        ),
    ]

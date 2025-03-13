# Generated by Django 2.1 on 2021-02-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='Book_name',
            field=models.CharField(max_length=30, verbose_name='Book name'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='Edition',
            field=models.CharField(max_length=30, verbose_name='Edition'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='Subject_name',
            field=models.CharField(max_length=10, verbose_name='Subject name'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='author_name',
            field=models.CharField(max_length=30, verbose_name='Author name'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='review',
            field=models.CharField(max_length=30, verbose_name='Review'),
        ),
    ]

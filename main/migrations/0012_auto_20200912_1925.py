# Generated by Django 2.2.12 on 2020-09-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200911_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
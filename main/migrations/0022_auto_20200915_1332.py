# Generated by Django 2.2.12 on 2020-09-15 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200914_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category',
        ),
    ]

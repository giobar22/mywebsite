# Generated by Django 2.2.12 on 2020-09-26 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20200924_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
    ]

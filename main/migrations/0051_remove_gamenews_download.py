# Generated by Django 2.2.12 on 2020-10-16 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20201016_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamenews',
            name='download',
        ),
    ]

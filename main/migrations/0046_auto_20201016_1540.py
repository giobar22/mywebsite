# Generated by Django 2.2.12 on 2020-10-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_gamenews_download_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamenews',
            name='download_count',
            field=models.IntegerField(),
        ),
    ]

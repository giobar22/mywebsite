# Generated by Django 2.2.12 on 2020-10-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_remove_gamenews_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenews',
            name='download',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

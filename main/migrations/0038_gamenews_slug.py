# Generated by Django 2.2.12 on 2020-10-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20201008_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenews',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]

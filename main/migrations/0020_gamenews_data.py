# Generated by Django 2.2.12 on 2020-09-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_gamenews_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenews',
            name='data',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

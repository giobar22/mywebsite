# Generated by Django 2.2.12 on 2020-09-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_upcominggames'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcominggames',
            name='main_image2',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

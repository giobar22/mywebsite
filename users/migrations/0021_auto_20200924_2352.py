# Generated by Django 2.2.12 on 2020-09-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200924_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default/default.jpg', upload_to='profile_pics'),
        ),
    ]
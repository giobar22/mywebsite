# Generated by Django 2.2.12 on 2020-09-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200924_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='gallery/main/images/profile_pics/default/'),
        ),
    ]

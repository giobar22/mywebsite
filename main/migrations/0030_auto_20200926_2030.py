# Generated by Django 2.2.12 on 2020-09-26 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_comment_subcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='subcomment',
            name='news',
        ),
        migrations.RemoveField(
            model_name='subcomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='SubComment',
        ),
    ]
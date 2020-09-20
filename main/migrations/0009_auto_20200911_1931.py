# Generated by Django 2.2.12 on 2020-09-11 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='categories',
        ),
        migrations.AddField(
            model_name='categories',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Genre'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='gamenews',
            name='genres',
        ),
        migrations.AddField(
            model_name='gamenews',
            name='genres',
            field=models.ManyToManyField(to='main.Genre'),
        ),
    ]

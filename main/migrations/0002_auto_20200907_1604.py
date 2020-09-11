# Generated by Django 2.2.12 on 2020-09-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='gamenews',
            name='genres',
            field=models.ManyToManyField(to='main.Genre'),
        ),
    ]

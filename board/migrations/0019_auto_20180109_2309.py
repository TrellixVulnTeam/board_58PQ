# Generated by Django 2.0.1 on 2018-01-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_remove_post_photo2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.TextField(blank=True, max_length=100, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='post',
            name='metro',
            field=models.TextField(blank=True, max_length=100, verbose_name='Станция метро'),
        ),
    ]
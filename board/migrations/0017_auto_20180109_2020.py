# Generated by Django 2.0.1 on 2018-01-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_auto_20180109_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photo/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
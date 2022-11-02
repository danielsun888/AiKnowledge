# Generated by Django 3.2 on 2022-01-27 01:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_comment_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.AddField(
            model_name='articles',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos'),
            preserve_default=False,
        ),
    ]

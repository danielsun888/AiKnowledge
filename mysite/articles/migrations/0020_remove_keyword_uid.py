# Generated by Django 4.1.3 on 2022-11-24 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0019_keyword"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="keyword",
            name="uid",
        ),
    ]

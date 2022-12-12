# Generated by Django 4.1.3 on 2022-12-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_nickname_remove_user_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("zh-hans", "简体中文")],
                default="en",
                max_length=10,
            ),
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0014_alter_articles_desc_alter_articles_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articles",
            name="url",
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]

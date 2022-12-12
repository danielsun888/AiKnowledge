# Generated by Django 4.1.3 on 2022-12-12 01:44

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Articles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.TextField(blank=True, null=True, verbose_name="title"),
                ),
                ("bookID", models.BigIntegerField(blank=True, null=True)),
                ("chapterID", models.BigIntegerField(blank=True, null=True)),
                (
                    "chapterName",
                    models.TextField(blank=True, null=True, verbose_name="chapterName"),
                ),
                ("VerseID", models.BigIntegerField(blank=True, null=True)),
                ("text", models.TextField(blank=True, null=True, verbose_name="name")),
                ("BookName", models.TextField(blank=True, null=True)),
                ("Volume", models.TextField(blank=True, null=True)),
                (
                    "keywords",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=10), size=8
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("bookID", models.IntegerField(blank=True, null=True)),
                ("totalChapters", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, verbose_name="name")),
                ("frequency", models.BigIntegerField(verbose_name="frequency")),
            ],
        ),
       
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=False)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="articles.articles",
                    ),
                ),
            ],
            options={
                "ordering": ["updated"],
            },
        ),
        migrations.CreateModel(
            name="Chapters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("chapterID", models.IntegerField(blank=True, null=True)),
                ("bookName", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "testament",
                    models.CharField(
                        choices=[("old", "old testament"), ("new", "new testament")],
                        default="old",
                        max_length=20,
                    ),
                ),
                (
                    "Book",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.book",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="articles",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="articles.book",
            ),
        ),
        migrations.AddField(
            model_name="articles",
            name="chapter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="articles.chapters",
            ),
        ),
        migrations.AddField(
            model_name="articles",
            name="manyKeywords",
            field=models.ManyToManyField(to="articles.keyword"),
        ),
    ]

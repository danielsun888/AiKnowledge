# Generated by Django 4.1.3 on 2022-12-08 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User2",
            new_name="User",
        ),
    ]

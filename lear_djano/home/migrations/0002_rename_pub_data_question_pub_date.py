# Generated by Django 5.2.4 on 2025-07-22 02:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="pub_data",
            new_name="pub_date",
        ),
    ]

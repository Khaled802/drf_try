# Generated by Django 4.1.7 on 2023-02-19 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_upvote"),
    ]

    operations = [
        migrations.CreateModel(
            name="Downvote",
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
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="down_upvote",
                        to="app.post",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
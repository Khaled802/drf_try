# Generated by Django 4.1.7 on 2023-02-19 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="Upvote",
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
                        related_name="post_upvote",
                        to="app.post",
                    ),
                ),
            ],
        ),
    ]

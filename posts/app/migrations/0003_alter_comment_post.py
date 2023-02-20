# Generated by Django 4.1.7 on 2023-02-18 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_data_posted_post_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_comments",
                to="app.post",
            ),
        ),
    ]
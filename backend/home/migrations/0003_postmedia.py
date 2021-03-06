# Generated by Django 2.2.26 on 2022-05-10 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostMedia",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.URLField()),
                ("video", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="postmedia_post",
                        to="home.Post",
                    ),
                ),
            ],
        ),
    ]

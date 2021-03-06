# Generated by Django 2.2.26 on 2022-05-10 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_reportuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="followers",
            field=models.ManyToManyField(
                blank=True, related_name="user_followers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="user_following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

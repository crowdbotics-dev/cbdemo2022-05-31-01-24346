from django.conf import settings
from django.db import models


class Post(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="post_user",
    )
    caption = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class PostMedia(models.Model):
    "Generated Model"
    post = models.ForeignKey(
        "home.Post",
        on_delete=models.CASCADE,
        related_name="postmedia_post",
    )
    image = models.URLField()
    video = models.URLField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class ReportPost(models.Model):
    "Generated Model"
    post = models.ForeignKey(
        "home.Post",
        on_delete=models.CASCADE,
        related_name="reportpost_post",
    )
    reported_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reportpost_reported_by",
    )
    reason = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

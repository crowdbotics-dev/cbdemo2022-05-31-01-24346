from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    email = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class BlockUser(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="blockuser_user",
    )
    blocked_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="blockuser_blocked_by",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class ReportUser(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reportuser_user",
    )
    reported_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reportuser_reported_by",
    )
    reason = models.TextField()

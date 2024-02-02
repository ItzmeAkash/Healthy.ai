from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class DietRecommendServices(AbstractUser, PermissionsMixin):
    GENDER_CHOICES = [
        ("Male", _("Male")),
        ("Female", _("Female")),
    ]
    ACTIVITY_CHOICES = [
        ('sedentary', _('Sedentary')),
        ('light', _('Light')),
        ('moderately', _('Moderately active')),
        ('very', _('Very active')),
        ('extreme', _('Extremely active')),
    ]
    GOAL_CHOICES = [
        ('weightloss', _('Weight Loss')),
        ('weightgain', _('Weight Gain')),
        ('maintainweight', _('Maintain Weight')),
    ]

    age = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    physical_activity = models.CharField(max_length=100, choices=ACTIVITY_CHOICES)
    goal = models.CharField(max_length=100, choices=GOAL_CHOICES)

    def __str__(self):
        return f"{self.username} - {self.age} years old"

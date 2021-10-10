from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Profile(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    user = models.OneToOneField(User, models.CASCADE)
    avator = models.ImageField(upload_to='avator', unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='male')
    birthday = models.DateField(null=True, blank=True, default=now)

    def __str__(self):
        return self.user.username

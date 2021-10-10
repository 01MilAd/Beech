from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Story(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=100)
    sound = models.FileField(upload_to='music', unique=True, null=True, blank=True)
    cover = models.ImageField(upload_to='picture', unique=True, null=True, blank=True)
    caption = RichTextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'story'
        verbose_name_plural = 'stories'

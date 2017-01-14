# Standard Library imports
from __future__ import unicode_literals

# Django Imports
from django.utils import timezone
from django.db import models


# Model to update "About Me" without re-writing html
class About(models.Model):

    class Meta:
        verbose_name_plural = 'About'

    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    bio = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact'

    title = models.CharField(max_length=30)
    facebook = models.URLField()
    github = models.URLField()
    email = models.EmailField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

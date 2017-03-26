# Standard Library imports
from __future__ import unicode_literals

# Django Imports
from django.utils import timezone
from django.db import models

# Third Party Imports
from tinymce import HTMLField


# Model to store info about Fresh Start Development
class BrandInfo(models.Model):

    class Meta:
        verbose_name_plural = 'Brand Information'

    title = models.CharField(max_length=30)
    sub_header = models.CharField(max_length=120)
    description = HTMLField('description')
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


# Model to update "About Me" without re-writing html
class About(models.Model):

    class Meta:
        verbose_name_plural = 'About'

    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    bio = HTMLField('bio')
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class FunFact(models.Model):

    prompt = models.CharField(max_length=50)
    fun_fact = models.CharField(max_length=50)

    def __str__(self):
        return self.prompt


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact'

    title = models.CharField(max_length=30)
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    email = models.EmailField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

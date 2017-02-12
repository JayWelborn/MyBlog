# Standard library imports
from datetime import timedelta, datetime

# Django imports
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Class for blog entries
class Entry(models.Model):

    class Meta:
        verbose_name_plural = "Entries"

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    header_image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='entries', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Defines primary key and slug as components of url
        """
        args = (self.pk, self.slug)
        return reverse(self, args)

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=30) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def get_absolute_url(self):
        """
        Defines primary key and slug as components of url
        """
        args = (self.pk, self.slug)
        return reverse(self, args)

    def __str__(self):
        return self.title

# Standard library imports
from datetime import timedelta, datetime

# Django imports
from django.db import models
from django.utils import timezone


# Class for blog entries
class Entry(models.Model):

    class Meta:
        verbose_name_plural = "Entries"

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    body = models.TextField()
    category = models.ManyToManyField('blog.Category')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=30) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

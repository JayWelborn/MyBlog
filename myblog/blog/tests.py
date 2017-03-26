# Standard library imports
from datetime import timedelta

# Django imports
from django.test import TestCase
from django.utils import timezone

# Relative imports
from .models import Entry, Tag


def create_entry_with_tag(title, days):
    """
    creates blog entry with a category
    :param title: entry title
    :param days: days in future/past entry is published
    :param body: adds body to entry. default set to None
    :return: returns instance of Entry object from blog.models
    """
    time = timezone.now() + timedelta(days=days)

    # create instance of entry with category
    entry = Entry.objects.create(title=title, pub_date=time, body='body')
    entry.save()
    entry.tag.add(1)
    return entry


def create_entry_without_tag(title, days):
    """
    creates blog entry without a category
    :param title: entry title
    :param days: days in future/past entry is published
    :param body: adds body to entry. default set to None
    :return: returns instance of Entry from blog.models
    """
    time = timezone.now() + timedelta(days=days)

    # create entry without category
    entry = Entry.objects.create(title=title, pub_date=time, body='body')
    return entry


def create_tag_with_no_entries(title):
    """Creates category with no entries"""
    return Tag.objects.create(title=title)


def create_tag_with_entry(title):
    """Creates category with an Entry"""
    tag = Tag.objects.create(title=title)
    tag.save()
    tag.entry.add(1)
    return tag


class EntryMethodTests(TestCase):

    def test_was_published_recently_with_future_entry(self):
        """
        Ensure was_published_recently returns False for
        entry published in the future
        :return: bool
        """
        future_entry = create_entry_with_tag('Title', 30)
        self.assertIs(future_entry.was_published_recently(), False)

    def test_was_published_recently_with_old_entry(self):
        """
        Ensure was_published_recently returns false for old entry
        :return: bool
        """
        old_entry = create_entry_with_tag('Title', -30)
        self.assertIs(old_entry.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        Ensure was_published_recently returns true for recent entry
        :return: bool
        """
        entry = create_entry_with_tag('Title', -1)
        self.assertIs(entry.was_published_recently(), True)

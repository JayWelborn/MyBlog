# Django imports
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

# Relative imports
from .models import Entry


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """
        Return last 5 blog entries
        """
        latest_entries = Entry.objects.distinct()
        return latest_entries.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Entry
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """
        Return last 5 blog entries
        """
        return Entry.objects.distinct()

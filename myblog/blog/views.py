# Django imports
from django.views import generic
from django.utils import timezone

# Relative imports
from .models import Entry, Tag


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'
    model = Entry
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """
        Get list of tags
        :return: tags
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.distinct()
        return context

    def get_queryset(self):
        """
        Return blog entries sorted by date
        """
        entries = Entry.objects.distinct()
        return entries.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    """
    View single blog entry
    """
    model = Entry
    template_name = 'blog/detail.html'


class TagListView(generic.ListView):
    """
    View all entries assiciated with a certain tag
    """
    model = Tag
    template_name = 'blog/tag_list.html'
    context_object_name = 'tag_list'
    paginate_by = 5
    paginate_orphans = 2

    def get_queryset(self):
        return Tag.objects.distinct()


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'


class TestView(generic.TemplateView):
    template_name = 'blog/new-entry.html'

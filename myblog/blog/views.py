# Django imports
from django.views import generic
from django.utils import timezone

# Relative imports
from .models import Entry, Category


# TODO add categories to indexview and detailview to be passed to templates
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'
    model = Entry
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """
        Get list of categories
        :return: Categories
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.distinct()
        return context

    def get_queryset(self):
        """
        Return blog entries sorted by date
        Return
        """
        entries = Entry.objects.distinct()
        return entries.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Entry
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """

        """
        return Entry.objects.distinct()


class TestView(generic.TemplateView):
    template_name = 'blog/new-entry.html'

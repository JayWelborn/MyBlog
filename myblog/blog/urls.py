# Django imports
from django.conf.urls import url

# Relative imports
from .views import DetailView, IndexView, TestView, TagListView, TagDetailView

app_name = 'blog'
urlpatterns = [
    # ex: /blog/new-entry
    url(r'^new-entry/$', TestView.as_view(), name='test'),
    # ex: /blog/pk/entry-slug-goes-here
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', DetailView.as_view(), name='detail'),
    # ex /blog/tags
    url(r'^tags/$', TagListView.as_view(), name='tags'),
    # ex /blog/tags/pk/tag-slug-here
    url(r'tags/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/', TagDetailView.as_view(), name='tag_detail'),
    # ex: /blog/
    url(r'^$', IndexView.as_view(), name='index'),
]

# Django imports
from django.conf.urls import url

# Relative imports
from .views import DetailView, IndexView

app_name = 'blog'
urlpatterns = [
    # ex: /bingo/pk/entry-slug-goes-here
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', DetailView.as_view(), name='detail'),
    # ex: /bingo/
    url(r'^$', IndexView.as_view(), name='index'),
]

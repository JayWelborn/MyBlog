# Django imports
from django.conf.urls import url

# Relative imports
from .views import DetailView, IndexView

app_name = 'blog'
urlpatterns = [
    # ex: /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # ex: /blog/
    url(r'^$', IndexView.as_view(), name='index'),
]

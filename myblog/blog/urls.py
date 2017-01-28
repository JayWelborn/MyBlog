# Django imports
from django.conf.urls import url

# Relative imports
from .views import DetailView, IndexView, TestView

app_name = 'blog'
urlpatterns = [
    # ex: /blog/new-entry
    url(r'^new-entry/$', TestView.as_view(), name='test'),
    # ex: /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # ex: /blog/
    url(r'^$', IndexView.as_view(), name='index'),
]

# Django imports
from django.conf.urls import url

# Relative imports
from .views import IndexView, AboutView, ContactView

app_name = 'home'
urlpatterns = [
    # ex: [domain}/
    url(r'^$', IndexView.as_view(), name='index'),
    # ex: [domain]/about
    url(r'^about/$', AboutView.as_view(), name='about'),
    # ex: [domain]/contact
    url(r'^contact/$', ContactView.as_view(), name='contact'),
]

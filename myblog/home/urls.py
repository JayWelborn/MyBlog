# Django imports
from django.urls import path

# Relative imports
from .views import IndexView, AboutView, ContactView

app_name = 'home'
urlpatterns = [
    # ex: [domain}/
    path('', IndexView.as_view(), name='index'),
    # ex: [domain]/about
    path('about/', AboutView.as_view(), name='about'),
    # ex: [domain]/contact
    path('contact/', ContactView.as_view(), name='contact'),
]

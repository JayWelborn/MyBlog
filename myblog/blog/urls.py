# Django imports
from django.urls import path

# Relative imports
from .views import DetailView, IndexView, TestView, TagListView, TagDetailView

app_name = 'blog'
urlpatterns = [
    # ex: /blog/new-entry
    path('new-entry/', TestView.as_view(), name='test'),
    # ex: /blog/pk/entry-slug-goes-here
    path('<int:pk>/<slug:slug>/', DetailView.as_view(), name='detail'),
    # ex /blog/tags
    path('tags/', TagListView.as_view(), name='tags'),
    # ex /blog/tags/pk/tag-slug-here
    path('tags/<int:pk>/<slug:slug>/',
         TagDetailView.as_view(), name='tag_detail'),
    # ex: /blog/
    path('', IndexView.as_view(), name='index'),
]

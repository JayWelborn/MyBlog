# Django imports
from django.shortcuts import render
from django.views import generic

# Relative imports
from .models import About, Contact


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'home/index.html'

    def get_queryset(self):
        return []


class AboutView(generic.ListView):
    template_name = 'home/about.html'
    context_object_name = 'about'

    def get_queryset(self):
        return About.objects.latest('pub_date')


class ContactView(generic.ListView):
    template_name = 'home/contact.html'
    context_object_name = 'contact'

    def get_queryset(self):
        return Contact.objects.latest('pub_date')



# Django imports
from django.shortcuts import render
from django.views.generic import ListView, FormView

# Relative imports
from .models import About, Contact
from .forms import ContactForm


# Create your views here.
class IndexView(ListView):
    template_name = 'home/index.html'

    def get_queryset(self):
        return []


class AboutView(ListView):
    template_name = 'home/about.html'
    context_object_name = 'about'

    def get_queryset(self):
        return About.objects.latest('pub_date')


class ContactView(ListView, FormView):
    template_name = 'home/contact.html'
    context_object_name = 'contact'
    form_class = ContactForm
    success_url = '/contact/'

    def get_queryset(self):
        return Contact.objects.latest('pub_date')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

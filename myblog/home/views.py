# stdlib imports
import random

# Django imports
from django.shortcuts import render
from django.views.generic import ListView, FormView

# Relative imports
from .models import About, Contact, FunFact
from .forms import ContactForm


# Create your views here.
class IndexView(ListView):
    template_name = 'home/index.html'

    def get_queryset(self):
        return []


class AboutView(ListView):
    template_name = 'home/about.html'
    context_object_name = 'about'
    model = About

    def get_context_data(self, **kwargs):
        """
        Populate list with random fun facts about me
        """
        all_facts = FunFact.objects.distinct()

        context = super(AboutView, self).get_context_data(**kwargs)
        context['fun_fact_list'] = random.sample(list(all_facts), 3)
        return context

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

# stdlib imports
import random

# Django imports
from django.views.generic import ListView, FormView
from django.contrib import messages

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


class ContactView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    success_msg = 'Thanks for the Email!'

    def get_context_data(self, **kwargs):
        """
        Get list of info from Contact Model to be passed to view
        :return: latest contact information from db
        """
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.latest('pub_date')
        return context

    def form_valid(self, form):
        """
        Sends email and displays success message when a valid form
        is submitted.
        :param form: from .forms.py
        :return: instance of ContactView with success_msg attribute accessible for the view.
        """
        form.send_email()
        messages.info(self.request, self.success_msg)
        return super(ContactView, self).form_valid(form)

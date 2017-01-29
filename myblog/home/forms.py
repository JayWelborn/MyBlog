# Django Imports
from django import forms
from django.core.mail import send_mail, EmailMessage


# create a contact form to send email to my email address
class ContactForm(forms.Form):
    """
    The Contact form will allow users to send an email without
    clicking a mailto link.
    """
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=50, required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        """
        This function will send an email using the data from the form on my contact page
        :return: none
        """

        # instantiates EmailMessage class with data from form
        contact_email = EmailMessage(subject=self.cleaned_data['subject'],
                                     to=['jesse.welborn@gmail.com'],
                                     body='Sender Name: {} \nSender Email: {}\n\n {}'.format(
                                         self.cleaned_data['name'],
                                         self.cleaned_data['email'],
                                         self.cleaned_data['message']
                                     ))

        # adds cc line if applicable
        cc_myself = self.cleaned_data['cc_myself']
        if cc_myself:
            contact_email.cc = [self.cleaned_data['email']]

        # send email
        contact_email.send()

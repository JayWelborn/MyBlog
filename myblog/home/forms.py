# Django Imports
from django import forms


# create a contact form to send email to my email address
class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

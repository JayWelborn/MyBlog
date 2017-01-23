# Django Imports
from django import forms


# create a contact form to send email to my email address
class ContactForm(forms.Form):

    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=50, required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        # send email
        print('email sent.')

        sender = self.email
        subject = self.subject
        message = self.message
        name = self.name

        #if self.cc_myself:
            # TODO

        pass

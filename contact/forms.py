from django import forms
from .models import Contact

class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_num', 'email', 'message']
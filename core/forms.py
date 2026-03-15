from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form — saves to DB and optionally sends email."""

    class Meta:
        model   = ContactMessage
        fields  = ['name', 'email', 'subject', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={
                'placeholder': 'Your Full Name',
                'class': 'form-input',
                'autocomplete': 'name',
            }),
            'email':   forms.EmailInput(attrs={
                'placeholder': 'abc@company.com',
                'class': 'form-input',
                'autocomplete': 'email',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Internship / Job Inquiry',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about the opportunity...',
                'class': 'form-textarea',
                'rows': 5,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Name must be at least 2 characters.')
        return name

    def clean_message(self):
        msg = self.cleaned_data.get('message', '').strip()
        if len(msg) < 1:
            raise forms.ValidationError('Message must be at least 10 characters.')
        return msg

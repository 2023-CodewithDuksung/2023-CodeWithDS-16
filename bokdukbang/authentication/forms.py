from django import forms
from django.contrib.auth.forms import AuthenticationForm

class DuksungEmailAuthenticationForm(AuthenticationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith('@duksung.ac.kr'):
            raise forms.ValidationError("You must use a @duksung.ac.kr email address.")

        return email

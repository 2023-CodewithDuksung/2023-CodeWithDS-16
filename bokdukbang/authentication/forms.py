from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class DuksungEmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")

        self.user_cache = User.objects.get(email=email)

        return cleaned_data

    def get_user(self):
        return self.user_cache

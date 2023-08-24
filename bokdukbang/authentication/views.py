from django.contrib.auth.views import LoginView
from .forms import DuksungEmailAuthenticationForm

class DuksungLoginView(LoginView):
    form_class = DuksungEmailAuthenticationForm




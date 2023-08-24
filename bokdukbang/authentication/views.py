from django.contrib.auth.views import LoginView
from .forms import DuksungEmailAuthenticationForm

class DuksungLoginView(LoginView):
    form_class = DuksungEmailAuthenticationForm
    template_name = 'authentication/login.html'
    success_url = '/chooselocation/'

from django.views.generic import TemplateView

class ChooseLocationView(TemplateView):
    template_name = 'authentication/chooselocation.html'

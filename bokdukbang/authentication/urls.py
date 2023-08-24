from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import DuksungLoginView, ChooseLocationView

app_name = 'authentication'
urlpatterns = [
    path('login/', DuksungLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('chooselocation/', ChooseLocationView.as_view(), name='chooselocation'),
]

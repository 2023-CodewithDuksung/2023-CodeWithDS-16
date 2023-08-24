from django.urls import path
from .views import DuksungLoginView

app_name = 'authentication'
urlpatterns = [
    path('login/', DuksungLoginView.as_view(), name='login'),
    path('logout/', DuksungLoginView.as_view(), name='logout'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes, name='quotes'),
]
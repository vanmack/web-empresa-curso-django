from django.urls import path
from . import views

urlpatterns = [
    #path de services
    path('', views.services, name="services"),
]
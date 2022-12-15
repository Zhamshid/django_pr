from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('persons', views.about, name="persons"),
    path('contacts', views.contacts, name="contacts")
]
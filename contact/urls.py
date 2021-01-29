from django.urls import path
from . import views
from .views import (
    contact,
)



urlpatterns = [
    path('contact/', views.contact, name='contact_page'),

]

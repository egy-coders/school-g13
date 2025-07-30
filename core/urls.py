from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('courses/', courses, name='courses'),
    path('faqs/', faqs, name='faqs'),
]
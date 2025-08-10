from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('courses/', courses, name='courses'),
    path('courses/<int:course_id>/', course, name='course'),
    path('courese/create/', create_course, name='create_course'),

    path('cats/', cats, name='cats'),


    path('faqs/', faqs, name='faqs'),
]
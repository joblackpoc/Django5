from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('courses/', views.courses, name='courses'),
   path('contact/', views.contact, name='contact'),
   path('instructors/', views.instructors, name='instructors'),
]

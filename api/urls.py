from django.urls import path
from .views import get_students, get_subjects

urlpatterns = [
    path('students/', get_students),
    path('subjects/', get_subjects),
    
]

from django.urls import path
from core import views

urlpatterns = [
    path('api/changes/', views.hello, name='changes'),
]

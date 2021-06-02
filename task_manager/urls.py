from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', Dashboard, name='dashboard'),
    path('additional/<str:pk>', Additional, name='additional')
]

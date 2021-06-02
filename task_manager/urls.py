from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', Dashboard, name='dashboard'),
    path('single/<str:pk>', SingleTask, name='single-task'),
    path('additional/<str:pk>', Additional, name='additional'),
    path('delete/<str:pk>', DeleteTask, name='delete-task'),
    path('add-comment/<str:pk>', AddComment, name='add-comment'),
]

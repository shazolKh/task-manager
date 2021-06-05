from django.urls import path
from .views import *

urlpatterns = [
    path('manager/', Dashboard, name='dashboard'),
    path('<str:pk>', SingleTask, name='single-task'),
    path('delete/<str:pk>', DeleteTask, name='delete-task'),
    path('add-comment/<str:pk>', AddComment, name='add-comment'),
    path('approve/<str:pk>', Approve, name='approve'),
    path('add-task/', AddTask, name='add-task'),
    path('summary/', Summary, name='summary'),
    path('dashboard/', MainDashboard, name='main-dashboard'),

    path('search/', Search, name='search')
]

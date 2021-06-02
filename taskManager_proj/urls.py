from django.contrib import admin
from django.urls import path, include
from task_manager.views import Additional

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('task/', include('task_manager.urls')),
    # path('additional/<str:pk>/', Additional, name='additional')
]

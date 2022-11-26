from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<str:id>/', views.updateTask, name='update_task'),
    path('delete_task/<str:id>/', views.deleteTask, name='delete_task'),
]

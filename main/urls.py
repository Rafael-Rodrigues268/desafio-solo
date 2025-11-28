from django.urls import path
from . import views

urlpatterns = [
    path ('', views.task_list,name='task_list'),
    path('concluidas/',views.task_concluidas,name='task_concluidas'),
    path('pendentes/',views.task_pendentes,name='task_pendentes'),
    path('create_task',views.task_create,name='task_crate'),
]

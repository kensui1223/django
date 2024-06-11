from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    path('new/', views.student_create, name='student_create'),
    path('edit/<str:id>/', views.student_update, name='student_update'),
    path('delete/<str:id>/', views.student_delete, name='student_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('add/', views.user_add, name='user_add'),
    path('edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('users/export/', views.export_users_csv, name='export_users_csv')

]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='signup'),
    path('login/', views.login_page, name='login'),
    path('todopage/',views.todo, name='todo'),
    path('edit_todo/<int:id>', views.edit_todo, name='edit_todo'),
    path('delete/<int:srno>', views.delete_todo, name='delete_todo'),
    path('logout/', views.user_logout, name='logout'),
]

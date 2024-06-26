from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('objects/', views.object_list, name='object_list'),
    path('objects/create/', views.object_create, name='object_create'),
    path('objects/<int:id>/edit/', views.object_edit, name='object_edit'),
    path('objects/<int:id>/delete/', views.object_delete, name='object_delete'),
    path('chat/', views.chat_view, name='chat'),
]

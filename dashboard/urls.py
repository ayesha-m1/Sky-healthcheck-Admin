from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('team-department/', views.team_department_view, name='team_department'),
    path('view-user/', views.view_user, name='view_user'),
    path('view-session/', views.view_session, name='view_session'),
]
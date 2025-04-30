from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
<<<<<<< HEAD
    path('team-department/', views.team_department_view, name='team_department'),
    path('view-user/', views.view_user, name='view_user'),
    path('view-session/', views.view_session, name='view_session'),
=======
path('team-department/', views.team_department_view, name='team_department'),
    path('view-user/', views.view_user, name='view_user'),
    path('view-session/', views.view_session, name='view_session'),
      path('login/', views.login, name='login'),
         path('signup/', views.signup, name='signup'),
          path('api/team-members/', views.team_members, name='team_members'),
    path('api/add-member/', views.add_member, name='add_member'),
    path('api/delete-team/', views.delete_team, name='delete_team'),
>>>>>>> 094fb77 (DATA BASE ADDED FOR DATA)
]
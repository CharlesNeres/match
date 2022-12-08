from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('match/<int:pk>/', views.match_detail, name='match_detail'),
    path('edit-match/<int:pk>/', views.edit_match, name='edit_match'),
    path('delete-match/<int:pk>/', views.delete_match, name='delete_match'),
    path('edit-player/<int:pk>/', views.edit_player, name='edit_player'),
    path('delete-player/<int:pk>/', views.delete_player, name='delete_player'),
    path('match/<int:pk>/generate-team/', views.generate_team, name='generate_team'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),  # Handles /app/
    path('create/', views.tweet_create, name='tweet_create'),  
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),  
    path('<int:tweet_id>/delete/', views.tweet_del, name='tweet_del'),  
    path('register/', views.register, name='reg'),  
    path('search/', views.search, name='search'),  
    
]

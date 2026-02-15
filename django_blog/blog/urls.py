from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    
    path('register/', views.register, name= 'register'),
    path('profile/', views.profile, name= 'profile'),

    # Login and Logout URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),


    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),

    path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),

    path("comments/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),


    ]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView  

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    
    path('register/', views.register, name= 'register'),
    path('profile/', views.profile, name= 'profile'),

    # Login and Logout URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),


     # Comment URLs (ALX REQUIRED FORMAT)

    # Create
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment_create"
    ),

    # Update
    path(
        "comment/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="comment_update"
    ),

    # Delete
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment_delete"
    ),

    ]
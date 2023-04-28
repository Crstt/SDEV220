from django.urls import path
from . import views

from django.contrib.auth import views as vAuth

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('accounts/login/', vAuth.LoginView.as_view(), name='login'),
    path('accounts/logout/', vAuth.LogoutView.as_view(next_page='/'), name='logout'),
]
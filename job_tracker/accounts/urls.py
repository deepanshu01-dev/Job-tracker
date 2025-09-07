from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.signup_view, name='register'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('delete/', views.delete_account, name='delete'),
]


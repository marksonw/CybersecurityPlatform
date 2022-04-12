from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.registerUser, name='register'),
    # path('login/', views.loginUser, name='login'),
    # path('logout/', views.logoutUser, name='logout'),
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('user-account/', views.userAccount, name="user-account"),
    path('edit-profile/', views.editAccount, name="edit-profile"),
    path('create-interests/', views.createInterest, name="create-interests"),
    # path('delete-interests/<str:pk>/', views.deleteInterest, name="delete-interests"),
    
]

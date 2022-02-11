from unicodedata import name
from django.urls import path
from .import views


urlpatterns = [

        path('', views.researchs, name="researchs"),
        path('research/<str:pk>/', views.research, name="research"),
        path('create-research/', views.createResearch, name="create-research"),
        
]
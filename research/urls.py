from django.urls import path
from .import views


urlpatterns = [
        path('research/', views.research, name="research"),
]
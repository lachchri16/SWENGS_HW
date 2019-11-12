from django.urls import path
from . import views

urlpatterns = [
    path('CPU/', views.cpu_default),
    path('CPU/<int:pk>/', views.cpu_pk)
]

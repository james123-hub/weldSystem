from django.urls import path
from .import views

urlpatterns = [
    path('', views.picProcess, name = 'picProcess'),
    path('edit/', views.test, name = 'test'),
    path('cut/', views.piccut, name = 'piccut')
]
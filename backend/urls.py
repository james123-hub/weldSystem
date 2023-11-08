from django.urls import path
from .import views

urlpatterns = [
    path('', views.userManage, name = 'userManage'),
    path('dataManage/',views.dataManage, name = 'dataManage')
]
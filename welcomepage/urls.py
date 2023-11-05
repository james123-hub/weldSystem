from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name= 'homepage'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name = 'home'),
    path('logout/', views.logout, name = 'logout'),
    path('cookie/', views.getCookie, name = 'cookie'),
    path('base/',views.getBase, name = 'base'),
    path('userdetail/', views.userDeatail, name = 'userdetail'),
    path('editPwd/', views.editPwd, name = 'editPwd')
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('detail',views.detail,name='detail'),
    path('logout',views.logout,name='logout'),
]

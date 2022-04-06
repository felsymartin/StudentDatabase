from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login',views.login,name ='login'),
    path('register',views.register, name='register'),
    path('detailsview<int:btch>/',views.detailsview, name='view'),
    path('idview',views.idview, name ='viaid')
    ]
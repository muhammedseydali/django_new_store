
from django.urls import path
from app import views

urlpatterns = [

    path('', views.emp, name='home'),
    path('register',views.register, name='register'),
    path('login',views.register, name='register')

]

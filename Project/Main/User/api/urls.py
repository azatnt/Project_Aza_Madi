from Api.views import *
from django.urls import path
from User.api.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', Register.as_view(), name= "register_url"),
    path('login', obtain_auth_token, name= "login_url"),

]

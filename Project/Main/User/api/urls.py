from Api.views import *
from django.urls import path
from User.api.views import *

urlpatterns = [
    path('register', Register.as_view(), name= "register_url"),

]

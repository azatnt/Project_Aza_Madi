"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from User import views as v
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('Miri.urls')),
    path('signup/', v.SignUp, name='signup_url'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login_url'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout_url'),
    path('', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

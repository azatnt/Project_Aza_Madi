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
    path('signup/', v.SignUp.as_view(), name='signup_url'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout_url'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login_url'),
    path('', include('django.contrib.auth.urls')),


    path('password_change/done',
        auth_view.PasswordChangeDoneView.as_view(template_name='Profile/password_changed.html'),
        name='password_change_done_url'),

    path('change_password/',
        auth_view.PasswordChangeView.as_view(template_name='Profile/password_change.html'),
        name='password_change_url'),

    path('reset_password/',
        auth_view.PasswordResetView.as_view(template_name='Profile/password_reset.html'),
        name='reset_password_url'),

    path('reset_password_sent/',
        auth_view.PasswordResetDoneView.as_view(template_name='Profile/password_reset_sent.html'),
        name='password_reset_done_url'),

    path('reset/<uidb64>/<token>/',
        auth_view.PasswordResetConfirmView.as_view(template_name='Profile/password_reset_form.html'),
        name='password_reset_confirm_url'),

    path('reset_password_complete/',
        auth_view.PasswordResetCompleteView.as_view(template_name='Profile/password_reset_done.html'),
        name='password_reset_complete_url'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

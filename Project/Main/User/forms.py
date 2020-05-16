from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *






class SignUpForm(UserCreationForm):
	# name = forms.CharField(max_length=120)
	# surname = forms.CharField(max_length=120)
	email = forms.EmailField()
	# phone = forms.CharField(max_length=50)


	class Meta:
		model = User
		fields = ['username',
				  'email',
				  'password1',
				  'password2']



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	# phone = forms.CharField(max_length=50)


	class Meta:
		model = User
		fields = ['username',
				  'email',
				  ]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

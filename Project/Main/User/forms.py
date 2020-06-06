from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *




class SignUpForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username',
				  'email',
				  'password1',
				  'password2']



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username',
				  'email',
				  ]

class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(required=False, widget=forms.FileInput)
	back_image = forms.ImageField(required=False, widget=forms.FileInput)

	class Meta:
		model = Profile
		fields = ['image',
				  'back_image',
				  ]


PAYMENT_CHOICES = (
	('C', 'CASH'),
	('C', 'CARD')
)

class UserAddressForm(forms.ModelForm):
	payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

	class Meta:
		model = UserAddress
		fields = ['address',
				  'address2',
				  'postcode',
				  'phone',
				  'payment_option',
				  ]

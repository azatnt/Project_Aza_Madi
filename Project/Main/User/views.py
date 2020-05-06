from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *




def SignUp(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! Now able to log in')
			return redirect('login_url')

	else:
		form = SignUpForm()
	return render(request, 'user/signup.html', context={'form':form})

	
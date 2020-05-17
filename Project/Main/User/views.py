from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *




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



@login_required
def profile(request):
	profile = Profile.objects.get_or_create(user=request.user)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile_url')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)



	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'user/profile.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404




class SignUp(View):
	form = SignUpForm
	template = 'user/signup.html'

	def get(self, request, *args, **kwargs):
		form = self.form()
		context = {'form' : form}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! Now able to log in')
			return redirect('login_url')
		context = {'form' : form}
		return render(request, self.template, context)




class Profile(View):
	model = Profile
	template = 'user/profile.html'

	def get(self, request, *args, **kwargs):
		profile = self.model.objects.get_or_create(user=request.user)
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		context = {
			'u_form': u_form,
			'p_form': p_form
		}
		return render(request, self.template, context)
		

	def post(self, request, *args, **kwargs):
		profile = self.model.objects.get_or_create(user=request.user)
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile_url')

		context = {
			'u_form': u_form,
			'p_form': p_form
		}
		return render(request, self.template, context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def registerview(request):
	form = RegisterForm()
	if request.method=='POST':
		form=RegisterForm(request.POST)
		#if form.is_valid():
		#	form.save()
		user = form.save()
		user.set_password(user.password) # set_password used to convert our password to hash password and then save the Database
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request, 'testApp/register.html',{'form':form})


@login_required
def dashbordview(request):
	return render(request, 'testApp/dashbord.html')
from django.shortcuts import render
from django.http import HttpRequest
from .forms import CreateUserForm

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# creating my logic here
def registerPage(request):
    form=CreateUserForm

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context={'form':form}
    return  render (request,'accounts/register.html', context)


# login logic here
def loginPage(request):
    context={}
    return  render (request,'accounts/login.html', context)
from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
# creating my logic here
def registerPage(request):
    context={}
    return  render (request,'accounts/register.html', context)


# login logic here
def loginPage(request):
    context={}
    return  render (request,'accounts/login.html', context)
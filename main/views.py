from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import CreateUserForm
from  django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# creating my logic here
def registerPage(request):
    form=CreateUserForm

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get("username")
            messages.info(request, 'Account was created for ' +  user)
            return redirect('login')

    context={'form':form}
    return  render (request,'accounts/register.html', context)


# login logic here
def loginPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context={}
    return  render (request,'accounts/login.html', context)

def home(request):
    content={}
    return render(request, 'home.html', content)
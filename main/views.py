from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import CreateUserForm
from  django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Category, NewsDetail

from django.contrib.auth.decorators import login_required
# Create your views here.
# creating my logic here
def registerPage(request):

    if request.user.is_authenticated:
        return redirect ('home')
    else:    
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
    if request.user.is_authenticated:
        return redirect ('home')
    else:  

        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            

            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect!!!, kindly check your details")
            
        context={}
        return  render (request,'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

  #home page here 
@login_required(login_url='login')
def home(request):
    # quering the category class
    categories=Category.objects.all()
    newsContents=NewsDetail.objects.all()
    content={'categories':categories, 'newsContents':newsContents}
    return render(request, 'home.html', content)


# the newsdetails template
def newsdetails(request,pk):
    contents=NewsDetail.objects.get(id=pk)
    context={'content':contents}
    return render(request,'newsdetails.html',context)

# the addnews temmplate
def addnews(request):
    categories=Category.objects.all()

    if request.method=="POST":
        data= request.POST
        image=request.FILES.get('image')

        if data['category']!='none':
            category=Category.objects.get(id=data['category'])
        elif data['newcategory'] !='':
            category, created=Category.objects.get_or_create(name=data['newcategory'])   
        else:
            category=None    

        newsdetail=NewsDetail.objects.create(
            category=category,
            description=data['description'],
            date_posted=data['date_posted'],
            postedby=data['postedby'],
            image=image


        )
        return redirect ('home')

    content={'categories':categories,}
    return render(request,'addnews.html',content)
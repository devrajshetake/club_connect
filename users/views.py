from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return HttpResponse("<h1>This is Home<h2>")

def login(request):
    if request.method == 'POST':
        user = auth.authenticate( username =request.POST['email'], password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            prof = Profile.objects.get(user= user)
            if prof.is_club_admin:
                return(redirect("club-home"))
            return redirect("home")
            # return render(request,'users/result.html')
        
        else:
            messages.error(request, "invalid login credentials")
            return redirect("LS")
    else:
        return redirect("LS")


def signup(request):
    # firstname = request.POST['first-name']
    # lastname = request.POST['last-name']
    # email = request.POST['email']
    # password  = request.POST['password']


    return render(request,'users/signup.html')

def logout(request):
    auth.logout(request)
    return redirect("home")

def LS(request):
    return render(request,'users/LS.html')

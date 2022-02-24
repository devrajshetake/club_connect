from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {}
    return render(request,'users/home.html',context)

def login(request):
    if request.method == 'POST':
        # print(request.POST['email']," ",request.POST['password'])
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate( username = email, password=password)
        print(user)
        if user is not None:
            # print(user.email)
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
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password  = request.POST['password']
        college = request.POST['college']
        mobile_number = request.POST['mobile']
        user = User.objects.create_user(username=email, email=email, first_name = firstname, password=password)

        newprofile = Profile.objects.create(user = user,college=college,mobile = mobile_number)
        
        user.save()
        newprofile.save()

    return render(request,'users/LS.html')

def logout(request):
    auth.logout(request)
    return redirect("home")

def LS(request):
    return render(request,'users/LS.html')

# def profile(request):
#     return HttpResponse("<h1>profile</h1>")

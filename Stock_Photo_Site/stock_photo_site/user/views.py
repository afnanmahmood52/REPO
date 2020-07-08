from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import *
from photo.models import Photo

# ----------------------
# Create your views here.
# ----------------------

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            print("Saving Form")
            form.save()
            
            return redirect("/home")
    else:
        print("Saving Form")
        form = RegisterForm()

    return render(response, "register.html" , {"form":form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request, user)
            return redirect("/home")

    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html" , {"form":form})


def logout_view(request):
        logout(request)
        return redirect("/home")


def view_account(request):

    # filter photos by current user logged in
    photo_objects = Photo.objects.filter(upload_by_id = request.user.username)
    
    context = {'photos':photo_objects}


    print(photo_objects[1])
    print(context)

    return render(request,'account_page.html',context)
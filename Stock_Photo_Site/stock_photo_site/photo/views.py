from django.shortcuts import render, redirect 
from django.http import request
from django.contrib.auth.decorators import login_required


# from .models import Photo
from .forms import UploadPhoto

# Create your views here.
@login_required(login_url="/login")
def upload_photo(request):

    if request.method == 'POST':
        form = UploadPhoto(request.POST,request.FILES)
        if form.is_valid():

            upload_photo = form.save(commit=False)
            print(upload_photo.title)
            print(upload_photo.desc)
            print(upload_photo.category_name)
            # print(upload_photo.upload_by)

            upload_photo.upload_by_id = request.user.username

            upload_photo.save()

            #form_copy = form.save(commit=False)
            #form_copy.Photo = request.Photo
            #form_copy.save()
            #form.save()
            return redirect('/home')
    
    else:
        form = UploadPhoto()
    context = {
        'form':form
    }

    return render(request, "upload_photo.html" , context)

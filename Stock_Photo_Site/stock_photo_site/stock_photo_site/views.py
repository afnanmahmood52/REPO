from django.http import HttpResponse
from django.http import request
from django.shortcuts import render
from photo.models import Photo
from django.db.models import Q
from category.models import Category

def home(request):
    # return HttpResponse("This is redirected to homepage")
    photo_objects = Photo.objects.all()
    photos_queried = Photo.objects.all()
    categories = Category.objects.all()

    query = request.GET.get("q")
    catg = request.GET.get("catg")
    
    print(categories)

    if query:
        photos_queried = photos_queried.filter(title__icontains=query,category_name__category_name=catg)

    context = {'photos_queried':photos_queried,'photos':photo_objects,'category':categories}
    #print(context)
    return render(request,'home.html',context)


def about(request):
    # return HttpResponse("This is redirected to about")
    return render(request,'home.html')



from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Details
from .forms import edit_form
# Create your views here.

# Home Page
def home_view(req):
    get_content=Details.objects.all()
    return render(req,'home.html',{'data':get_content})

# Fetch movie details individually
def get_movie(req,movie_id):
    get_data=Details.objects.get(id=movie_id)
    return render(req,'details.html',{'data':get_data})

# Add new movie to rhe list
def add_movie(req):
    if req.method=="POST":
        name=req.POST.get('name')
        title=req.POST.get('title')
        year=req.POST.get('year')
        img=req.FILES['poster']
        try:   
            data=Details(name=name,title=title,year=year,img=img)
            data.save()
            return redirect('/')
        except :
            return redirect('register')
    return render(req,"register.html")

# Edit existing movie details
def update(req,id):
    movie=Details.objects.get(id=id)
    if req.method=="POST":
        i=edit_form(req.POST or None,req.FILES,instance=movie)
        if i.is_valid():
            i.save()
            return redirect('/')
    else:
        i=edit_form(instance=movie)
    return render(req,"edit.html",{'data':i,'movie':movie})

# Delete Movie from the list
def delete_me(req,id):
    if req.method=="POST":
        try:
            get_data=Details.objects.get(id=id)
            get_data.delete()
            return redirect('/')
        except:
            return redirect('/')
    return render(req,'delete.html')
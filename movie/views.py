from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from movie.models import moviedatabase,user
# Create your views here.
def index(request):
    movie_obj=moviedatabase.objects.all()
    context={"data":movie_obj}
    return render(request,"index.html",context)
def review(request,pk):
     movie_obj=moviedatabase.objects.get(id=pk)
    
     user_obj=user.objects.filter()
     context={"data":movie_obj,"userdata":user_obj}
    
     if request.method== "POST":
        name = request.POST.get('name')
        description = request.POST.get('Description')
        rating=request.POST.get('range')
      
        user.objects.create(name=name,description=description,rating=rating,date=timezone.now())
     return render(request,"button.html",context)

def home(request):
    return render(request,"home.html")

def loginuser(request):
    if request.method=="POST":
        
        password=request.POST.get('password')
        username=request.POST.get('username')
        userobj=authenticate(username=username,password=password)
        if userobj:
            login(request,userobj)
            return redirect('home')
        else:
            return redirect('login')

    return render(request,"login.html")

def registeruser(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
        userobj=User.objects.create(email=email,username=username)
        userobj.set_password(password)
        userobj.save()

        return redirect('login')
    return render(request,"register.html")
def logoutuser(request):
    logout(request)
    return redirect('home')
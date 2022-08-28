from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import details
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
           if User.objects.filter(username=username).exists():
               messages.info(request,"username taken")
               return redirect('register')
           else:
             user=User.objects.create_user(username=username,password=password)
             user.save()
             return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('login')
    return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('detail')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def detail(request):
     if request.method == 'POST':
         name=request.POST.get('name',)
         dob=request.POST.get('dob',)
         age=request.POST.get('age',)
         gender=request.POST.get('gender',)
         mob_no = request.POST.get('mob', )
         email=request.POST.get('email',)
         address=request.POST.get('address',)
         department=request.POST.get('source',)
         course=request.POST.get('status',)
         purpose=request.POST.get('purpose',)
         detail=details(name=name,date_of_birth=dob,gender=gender,mob_no=mob_no,age=age,email=email,address=address,department=department,course=course,purpose=purpose)
         detail.save()


         messages.info(request,'Your order is placed')
     return render(request,'detail.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
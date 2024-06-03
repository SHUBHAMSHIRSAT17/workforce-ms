from django.shortcuts import render, redirect ,HttpResponse

from . forms import Employee_model
from . forms import Employee_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    if request.method == "POST":
        data = Employee_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect("/")

    else:
        fm = Employee_form
        return render(request, 'showform.html',{'form': fm})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def savedemo(request):
    if request.method == "POST":
        data = Employee_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        fm = Employee_form()
        return render(request, 'showform.html', {'form': fm})

def displaydata(request):
    data = Employee_model.objects.all()
    return render(request, 'display.html', {'res': data})


def edit(request, id):
    data = Employee_model.objects.get(id = id)
    return render(request, 'edit.html', {'res': data})


def updatedata(request, id):
    emp = Employee_model.objects.get(id=id)
    data = Employee_form(request.POST, instance=emp)
    if data.is_valid():
        data.save()
        return redirect('display')  # Redirect to the display page after updating

def deletedata(request, id):
    data = Employee_model.objects.get(id=id)
    data.delete()
    return redirect('display')  # Redirect to the display page after deleting
# Create your views here.
import re
from unicodedata import name
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib import auth,messages
from cart.models import Cart,CartItem
from django.http import JsonResponse
from app.otp import checkOTP, sentOTP
from .models import CustomUser,Address
from .forms import CustomUserForm,RegistrationForm,AddressForm,UserProfileForm,UserForm



def emp(request):

    return render(request, 'index.html' )

def register(request):

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')        

    # def show(request):
    #     employees = CustomUser.objects.all()
    #     return render(request, "show.html", {'employees': employees})
    #
    # def edit(request, id):
    #     employee = CustomUser.objects.get(id=id)
    #     return render(request, 'edit.html', {'employee': employee})
    #
    # def update(request, id):
    #     employee = CustomUser.objects.get(id=id)
    #     form = EmployeeForm(request.POST, instance=employee)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("/show")
    #     return render(request, 'edit.html', {'employee': employee})
    #
    # def destroy(request, id):
    #     employee = CustomUser.objects.get(id=id)
    #     employee.delete()
    #     return redirect("/show")

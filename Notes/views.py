from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate  , login ,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse , redirect
from django.contrib import messages


def login_page(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"INVALID USERNAME OR PASSWORD")
            return render(request,'login_page.html')
        login(request,user)
        return redirect('view_page')
    return render(request,"login_page.html")


def register_page(request):
    if(request.method=="POST"):
        FirstName=request.POST.get("firstname")
        LastName=request.POST.get("lastname")
        username=request.POST.get("username")
        password=request.POST.get("password")

        if User.objects.all().filter(username=username).exists():
            messages.error(request,"USERNAME ALREADY EXISTS")
            return render(request,'register_page.html')
        user=User.objects.create(first_name=FirstName,last_name=LastName,username=username)
        user.set_password(password)
        user.save()

    return render(request,"register_page.html")

@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect('login_page')
def home_page(request):
    return render(request,"home.html")

from .models import *

@login_required(login_url='/login/')
def add_notes(request):
    if(request.method=="POST"):
        text=request.POST.get("notes")
        print(text)
        note=Notes.objects.create(note=text,user=request.user)
        note.save()
        print("success")
    return render(request,'add_notes.html')

@login_required(login_url='/login/')
def view_notes(request):
    note=Notes.objects.all().filter(user=request.user)
    return render(request,"view_notes.html",context={"notes":note})

@login_required(login_url='/login/')
def edit_notes(request,id):
    queryset=Notes.objects.get(id=id)
    if queryset.user.username!=request.user.username:
        redirect('/view_page/')
    nota=queryset
    if request.method=="POST":
        note=request.POST.get("notes")
        queryset.note=note
        queryset.save()
        return redirect('view_page')
    return render(request,"edit_notes.html" , context={"nota":nota})


@login_required(login_url='/login/')
def delete_notes(request,id):
    queryset=Notes.objects.get(id=id)
    queryset.delete()
    return redirect('/view_page/')


def view_page(request):
    queryset=Notes.objects.filter(user__username=request.user.username)
    return render(request,"view_page.html",context={"queryset":queryset})
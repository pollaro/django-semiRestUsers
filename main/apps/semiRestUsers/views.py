from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Users

def index(request):
    context = {
        'allUsers':Users.objects.all()
    }
    return render(request,'semiRestUsers/index.html',context)

def new(request):
    return render(request,'semiRestUsers/newUser.html')

def edit(request,id):
    editUser = {
        'user':Users.objects.get(id=id)
    }
    return render(request,'semiRestUsers/editUser.html',editUser)

def create(request):
    Users.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],email=request.POST['emailAddress'])
    user_id = Users.objects.get(email=request.POST['emailAddress'])
    return redirect(reverse('show',args=[user_id.id]))

def show(request,id):
    details ={
        'user':Users.objects.get(id=id)
    }
    return render(request,'semiRestUsers/show.html',details)

def destroy(request,id):
    u = Users.objects.get(id=id)
    u.delete()
    return redirect(index)

def update(request,id):
    u = Users.objects.get(id=request.POST['userID'])
    u.firstName = request.POST['firstName']
    u.lastName = request.POST['lastName']
    u.email = request.POST['emailAddress']
    u.save()
    return redirect(reverse('show',args=[u.id]))

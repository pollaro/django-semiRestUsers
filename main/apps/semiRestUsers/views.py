from django.shortcuts import render, redirect

def index(request):
    return render(request,'semiRestUsers/index.html')

def new(request):
    return render(request,'semiRestUsers/new.html')

def edit(request,id):
    return render(request,'semiRestUsers/edit.html')

def create(request):
    return redirect()

def show(request,id):
    return render(request,'semiRestUsers/show.html')

def destroy(request,id):
    return redirect()

def update(request,id):
    return redirect()

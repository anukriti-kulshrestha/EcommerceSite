from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .form import SignupForm
from django.contrib.auth import authenticate,login as auth_login


# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,'home.html',{'count':count})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            name =  form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=name,password=raw_password)
            auth_login(request,user)
            return redirect('home')
    else:
        form = SignupForm()

    return render(request,'registration/signup.html',{'form':form})






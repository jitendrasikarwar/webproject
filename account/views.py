from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method =='POST':
        if request.POST['password1']== request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'account/signup.html',{'error':'your  username is take'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],email=request.POST['useremail'],password=request.POST['passward1'])
                auth.login(request,user)
                return render(request, 'account/signup.html', {'error': 'your data is saved successfuly..'})
        else:
            return render(request,'account/signup.html',{'error':'your paaword does not match'})
    else:
        return render(request,'account/signup.html')

def login(request):
    return render(request,'account/login.html')
def logout(request):
    return render(request,'account/signup.html')
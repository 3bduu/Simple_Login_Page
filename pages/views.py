from django.shortcuts import render ,redirect
from django.contrib.auth.models import User ,auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'templates/index.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect ('login')
    return render(request,'templates/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Alredy Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save();
                return redirect('login')        
        else:
            messages.info(request,'Passwords are not the same')
            return redirect('register')
    else:
        return render(request,'templates/register.html')
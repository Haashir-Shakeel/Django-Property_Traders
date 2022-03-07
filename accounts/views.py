from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        #get user values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']        
        password2 = request.POST['password2']

    	#checking password match

        if password == password2:
            #Check if username exists
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already in use ')
                else:
                    #looks good
                    user = User.objects.create_user(username=username,password=password,email=email,
                    first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,"You are successfully registered and can login now")
                    return redirect('login')
        else:
            messages.error(request, 'Passwords donot match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
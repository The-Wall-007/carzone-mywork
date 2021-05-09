from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from Contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"Welcome...")
            return redirect('dashboard_page')
        else:
            messages.error(request,"Email or Password are incorrect")
            return redirect('login_page')


    return render(request,"Accounts/login.html")

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,"Email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name = firstname,last_name=lastname,username=username,password=password,email=email)
                    auth.login(request, user)
                    messages.success(request,"Welcome...")
                    return redirect('dashboard_page')
                    user.save()
                    messages.success(request,"You are registered successfully")
                    return redirect('login')  

    return render(request,"Accounts/register.html")
@login_required(login_url='login_page')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    context = {
        'ui' : user_inquiry,
    }
    return render(request,"Accounts/dashboard.html",context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return redirect('home')
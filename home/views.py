from django.shortcuts import render, redirect

# added by adarsh

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html") 

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html" )

def contact(request):
    return render(request, "contact.html")

def prakruti(request):
    return render(request, "prakruti.html")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Matching user credentials
        user = authenticate(username = username, password = password)

        if user is not None:
            # dj authenticating id and pass
            login(request, user)
     
            return redirect('/prakruti') 

        else:
            # No backend authenticated the credentials
            error_message = "Invalid username or password! Please try again."
            messages.error(request, error_message)
            
            # return render(request, 'login.html')
            return render(request, "login.html", {"error_message" : error_message} )
        
    return render(request, "login.html")


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("cnf-password")

        # Check for username 
        if len(username) >10:
            error_msg1 = "Username must not be more than 10 characters"
            messages.error(request, error_msg1)

            return render(request, "signup.html", {"error_message" : error_msg1})
        
        # check for alphanumeric 
        if (not username.isalnum()):
            error_msg2 = "Username must be alpha-numeric"
            messages.error(request, error_msg2)

            return render(request, "register.html", {"error_message": error_msg2})
        
        # Checking for passwords match
        if pass1 != pass2:
            error_msg3 = "Passwords don't match!"
            messages.error(request, error_msg3)

            return render(request, "register.html", {"error_message" : error_msg3})
        
        # Checking for already existing users
        if (User.objects.filter(username=username).exists()):
            error_msg4 = "Username already taken! Please choose different one."
            messages.error(request, error_msg4)
            return render(request, "register.html", {"error_message": error_msg4})
        
        # Check for duplicated email 
        if (User.objects.filter(email=email).exists()):
            error_msg5 = "Email already taken! Please choose different one."
            messages.error(request, error_msg5)
            return render(request, "register.html", {"error_message ": error_msg5})
        
        # Creating user
        myUser = User.objects.create_user(username, email, pass2)
        myUser.save()
        success_msg = "Your a/c has been created successfully! "
        messages.success(request, success_msg)

        return redirect('/prakruti')
    
    return render(request, "register.html")


        










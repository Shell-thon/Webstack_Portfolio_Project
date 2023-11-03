from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.




def login_page(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username= email)

        if not user_obj.exists():
            messages.warning(request, "Account not found.")
            return HttpResponseRedirect(request.path_info)



        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect("/")



        messages.warning(request, 'Invalid credentials.')
        return HttpResponseRedirect(request.path_info)
    return render(request, "accounts/login.html")

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = ''  # Set last_name to an empty string
        email= request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username= email)

        if user_obj.exists():
            messages.warning(request, "Email already exists")
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email,)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "Check your inbox email sent to your mail.")
        return HttpResponseRedirect(request.path_info)

    

    return render(request, "accounts/register.html")
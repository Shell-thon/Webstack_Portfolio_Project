from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.




def login_page(request):
    return render(request, "accounts/login.html")

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email= request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username= email)

        if user_obj.exists():
            messages.info(request, "Email already exists")
            return render(request, "accounts/register.html")
    return render(request, "accounts/register.html")
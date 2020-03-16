from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Item
from django.contrib import messages
from django.contrib.auth.models import User, auth

app_name = 'core'


def home(request):
    context = {
        'item': Item.objects.all()
    }
    return render(request, 'core/home.html', context)


def index(request):
    return render(request, 'core/index.html')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product.html'


def contact(request):
    return render(request, 'core/contact.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('core:index')
        else:
            messages.info(request, 'Username OR Password is Incorrect')
            return redirect('core:login')
    else:
        return render(request, 'core/login.html')


def signupPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Address Already Exist')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                messages.info(
                    request, 'Congrats!! Account created for ' + username)
                return redirect('core:login')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('core:signup')
        return redirect('/')

    else:
        return render(request, 'core/signup.html')


def logoutPage(request):
    auth.logout(request)
    return redirect('core:login')

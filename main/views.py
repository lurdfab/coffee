from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    yes = AboutUs.objects.get(pk=1)

    form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message has been sent successfully')
            return redirect('home')
    

    context = {
        'yes':yes,
        'form':form,
    }
    return render(request, 'index.html', context)


@login_required
def about(request):
    ray = AboutUs.objects.get(pk=1)

    context = {
        'ray':ray,
    }

    return render(request, 'about_back.html', context)

@login_required
def menu(request):
    man = Menu.objects.all()

    context = {
        'man':man,
    }
    return render(request, 'menu.html', context)

def products(request):
    soul = Products.objects.all()
    # products = Reviews.objects.get(pk=products_id)
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            reviews = Reviews.objects.get(user__id=request.user.id, products__id=products)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank You! Your review has been updated')
            return redirect(url)

        except Reviews.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Reviews()
                data.comment = form.cleaned_data['comment']
                data.rating = form.cleaned_data['rating']
                data.products_id = products
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank You! Your review has been submitted')
                return redirect(url)

    context = {
        'soul':soul,
    }
    return render(request, 'products.html', context)

def signout(request):
    logout(request)
    messages.success(request, 'you are now signed out')
    return redirect('signin')

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('home')
        else:
            messages.error(request, 'username/password is incorrect please try again')
            return redirect('signin')
        
    return render(request, 'login.html')

def register(request):
    register=RegisterForm()
    if request.method =='POST':
        phone = request.POST['phone']
        address = request.POST['address']
        register = RegisterForm(request.POST)
        if register.is_valid():
            user = register.save()
            newuser = Register(user=user)
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.phone = phone
            newuser.address = address
            newuser.save()
            messages.success(request, f'congratulations {user.username} your account is created')
            return redirect('signin')
        
        else:
            messages.error(request, register.errors)
        
       

    return render(request, 'register.html')


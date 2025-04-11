from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signin_view(request):
    return render(request, 'signin.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')

def index(request):
    return render(request, 'index.html')

@login_required
def kindergarten(request):
    return render(request, 'kindergarten.html')

@login_required
def grades123(request):
    return render(request, 'grades123.html')

@login_required
def grades45(request):
    return render(request, 'grades45.html')

@login_required
def welcome_view(request):
    return render(request, 'welcome.html')

@login_required
def abc_songs(request):
    return render(request, 'ABC Songs.html')

@login_required
def math_songs(request):
    return render(request, 'math songs.html')

@login_required
def alphabet(request):
    return render(request, 'alphabet.html')

@login_required
def colors(request):
    color_list = [
        'red', 'green', 'blue', 'orange', 'purple',
        'yellow', 'pink', 'brown', 'teal',
        'black', 'gray', 'white'
    ]
    return render(request, 'color.html', {'colors': color_list})

@login_required
def numbers(request):
    return render(request, 'numbers.html')

@login_required
def shapes(request):
    return render(request, 'shapes.html')

def custom_login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        return redirect('/welcome/')

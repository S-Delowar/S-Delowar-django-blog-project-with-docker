from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from Registration_App.forms import SignupForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to the 'next' parameter if present, otherwise go to 'blogs'
            next_url = request.GET.get('next')  # Check for 'next' in GET parameters
            if next_url:
                return redirect(next_url)  # Redirect to the URL stored in 'next'
            else:
                return redirect('blogs')
            # return redirect('blogs')
    else:
        form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            # OR - in one step:
            user = form.get_user()
            # form.get_user Authenticates and fetches user in one step
            if user is not None:
                login(request, user)
                # Redirect to the 'next' parameter if present, otherwise go to 'blogs'
                next_url = request.GET.get('next')  # Check for 'next' in GET parameters
                if next_url:
                    return redirect(next_url)  # Redirect to the URL stored in 'next'
                else:
                    return redirect('blogs')  # Fallback to 'blogs' if no 'next' is provided
                # return redirect('blogs')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blogs')
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import SignUpForm
from django.contrib.auth import logout
from .forms import SignUpForm
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # This will load the Profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        return render(request, 'users/signup.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user.profile
        return render(request, 'users/profile.html', {'profile': profile})

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user.profile
        form = ProfileForm(instance=profile)
        return render(request, 'users/profile_form.html', {'form': form})

    def post(self, request):
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'users/profile_form.html', {'form': form})


def logout_view(request):
    logout(request) 
    return  redirect('login')
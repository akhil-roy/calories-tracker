from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html",{"form":form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,"user/profile.html",{"form":form})
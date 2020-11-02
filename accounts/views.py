from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from accounts.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def sign(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign.html', {'form': SignUpForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                request.POST['email'], request.POST['password2'])
            except IntegrityError:
                error = "This username is already taken. Try different one."
                return render(request, 'accounts/sign.html',
                              {'form': SignUpForm(), 'error': error})
            else:
                user.save()
                login(request, user)
                return redirect('home')
        else:
            error = "Passwords didn't match. Try again."
            return render(request, 'accounts/sign.html',
                          {'form': SignUpForm(), 'error': error})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

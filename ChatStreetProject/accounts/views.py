from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm


def signupaccount(request):
    if request.method == 'GET':
        # render sign up page with an empty form
        form = UserCreateForm()
        return render(request, 'signupaccount.html', {'form': form})
    elif request.method == 'POST':
        # validate sign up form data
        form = UserCreateForm(request.POST)
        if form.is_valid():
            # create a new user instance and save it to the database
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1']
                )
                user.save()
            except IntegrityError:
                return render(request, 'signupaccount.html',
                              {'form': form, 'error': 'Username already taken.'})
            # log in the new user and redirect to the chatroom page
            login(request, user)
            return redirect('loginaccount')
        else:
            # render the sign up page with the invalid form and error messages
            return render(request, 'signupaccount.html', {'form': form})

def logoutaccount(request):
    logout(request)
    return redirect('loginaccount')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',
                      {'form':AuthenticationForm})
    else:

        #username = request.POST.get('username')

        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',
                          {'form': AuthenticationForm(),
                           'error': 'username and password do not match'})
        else:
            login(request,user)
            return redirect('chatroom')

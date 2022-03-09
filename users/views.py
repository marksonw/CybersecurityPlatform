from email import message
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Interests, Profile



## Register
# def registerUser(request):
#     if request.user.is_authenticated:
#         return redirect('profiles')
#     else:
#         page = 'register'
#         form = CustomUserCreationForm()
#         if request.method == "POST":
#             form = CustomUserCreationForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.username = user.username.lower()
#                 user.save()

#                 messages.success(request, "Your account was successfully created! ")

#                 login(request, user)

#                 return redirect('profiles')
#             else:
#                 messages.error(request,"Something went wrong during registration!")

#         context = {'page': page, 'form':form}
#         return render(request, 'users/login.html', context)


## Logout
# @login_required(login_url='login')
# def logoutUser(request):
#     logout(request)
#     messages.error(request, "User was logged out!")
#     return redirect ('login')

# ## Login
# def loginUser(request):
#     if request.user.is_authenticated:
#         return redirect('profiles')
#     else:
#         page = 'login'
#         if request.user.is_authenticated:
#             return redirect('profiles')

#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']

#             try:
#                 user: User.objects.get(username=username)

#             except:
#                 messages.error(request, "User does not exist!")

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('profiles')
#             else:
#                 messages.error(request, "Username/Password is not valid!")

#         return render(request, 'users/login.html')

@login_required(login_url='accounts/login/')
def profiles(request):
    profiles = Profile.objects.all()
    interests = Interests.objects.all()
    context = {'profiles': profiles, 'interests': interests}
    return render(request, 'users/profile.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    interests = profile.interests_set.all()

    context = {'profile': profile, 'interests': interests,}

    return render(request, 'users/user-profile.html', context)
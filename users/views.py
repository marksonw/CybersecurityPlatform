from code import interact
from email import message
from multiprocessing import context
import profile
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, InterestForm
from .models import Interests, Profile
from .utils import searchProfiles




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
    profiles, search_query, Interests = searchProfiles(request)
    context = {'profiles': profiles, 'search_query': search_query, 'interests': Interests}
    return render(request, 'users/profile.html', context)

@login_required(login_url='accounts/login/')
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    interests = profile.interests_set.all()

    context = {'profile': profile, 'interests': interests,}

    return render(request, 'users/user-profile.html', context)

@login_required(login_url='accounts/login/')
def userAccount(request):
    profile = request.user.profile
    interests = profile.interests_set.all()

    context = {'profile': profile, 'interests': interests}
    return render(request, 'users/account.html', context)

@login_required(login_url='accounts/login/')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()

            return redirect('user-account')

    context = {"form": form}
    return render(request, 'users/edit-profile.html', context)

@login_required(login_url='accounts/login/')
def createInterest(request):
    profile = request.user.profile
    form = InterestForm

    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.owner = profile
            interest.save()
            messages.success(request, 'Skill was added')
            return redirect('user-account')

    context = {"form": form}
    return render(request, "users/interests_form.html", context)


# def deleteInterest(request, pk):
#     profile = request.user.profile
#     interest = profile.interests_set.get(id=pk)

#     if request.method == "POST":
#         interest.delete()
#         return redirect('user-account')
        
#     context ={"object": interest}
#     return render(request, "delete.html", context)
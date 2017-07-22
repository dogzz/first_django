from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from first_app.forms import DUserForm, UserProfileInfoForm
from first_app.models import AccessRecord, User, UserProfileInfo
from first_app import forms


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def users(request):
    users_list = User.objects.order_by('first_name')
    date_dict = {'users_list': users_list}
    return render(request, 'first_app/users.html', context=date_dict)

@login_required
def add_user(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'first_app/add_user.html', {'form': form})


def register(request):
    registered = False
    if request.method == "POST":
        user_form = DUserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = DUserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'first_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print('Login failed')
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'first_app/login.html', {})

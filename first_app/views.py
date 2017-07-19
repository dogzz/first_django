from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app import forms
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


def users(request):
    users_list = User.objects.order_by('first_name')
    date_dict = {'users_list': users_list}
    return render(request, 'first_app/users.html', context=date_dict)


def add_user(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'first_app/add_user.html', {'form': form})
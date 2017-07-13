from django.shortcuts import render
from second_app import forms
# Create your views here.

def index(request):
    return render(request, 'second_app/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation good')
            print(form.cleaned_data['name'])
    return render(request, 'second_app/form_page.html', {'form': form})
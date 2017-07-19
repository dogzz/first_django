from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'third_app/index.html', context_dict)


def relative(request):
    return render(request, 'third_app/relative.html')


def other(request):
    return render(request, 'third_app/other.html')
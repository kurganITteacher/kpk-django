from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    pass


def basket(request):
    pass


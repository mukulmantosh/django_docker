from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("<h1>hello world. This code is working !!</h1>")

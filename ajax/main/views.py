from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def search(request, search):
    return render(request, "main/extra.html", {
        "data": search
    })


def searchEmpty(request):
    return HttpResponse("No result")

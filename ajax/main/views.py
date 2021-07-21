from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def search(request, search):
    if search is not None:
        return render(request, "main/extra.html", {
            "data": search
        })
    else:
        return HttpResponse("No results")


def searchEmpty(request):
    return HttpResponse("No result")

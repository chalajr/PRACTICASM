from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def search(request, search):
    if request.user.is_authenticated:
        return render(request, "main/extra.html", {
            "user": request.user,
            "data": search
        })
    else:
        return HttpResponse("ESTAS PENDEJO")


def searchEmpty(request):
    return HttpResponse("No result")

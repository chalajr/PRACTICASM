from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, "main/index.html")


def search(request, search):
    list
    if request.user.is_authenticated:
        return render(request, "main/extra.html", {
            "user": request.user,
            "data": search
        })
    else:
        return HttpResponse("Necesitas autenticarte")


def searchEmpty(request):
    return HttpResponse("No result")

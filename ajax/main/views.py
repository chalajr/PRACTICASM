from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import example
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "main/index.html")


@login_required()
def search(request, search, page):
    listOfItems = Paginator(
        example.objects.filter(title__icontains=f"{search}"), 2)

    return render(request, "main/extra.html", {
        "user": request.user,
        "page_obj": listOfItems.page(page)
    })


def searchEmpty(request):
    return HttpResponse("No result")

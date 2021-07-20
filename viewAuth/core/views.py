from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms


def listing(request):
    data = {
        "blogs": models.Blog.objects.all(),
    }

    return render(request, "core/listing.html", data)


def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    data = {
        "blog": blog,
    }

    return render(request, "core/view_blog.html", data)


def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")


def user_registration(request):

    return render(request, "core/registration.html", {
        "employee": forms.EmployeeForm,
        "user": forms.UserForm
    })

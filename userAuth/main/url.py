from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard, name="dashboard"),
]

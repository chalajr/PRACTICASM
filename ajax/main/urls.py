from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('search/', views.searchEmpty, name="searchEmpty"),
    path('search/<str:search>/<int:page>', views.search, name="search"),
]

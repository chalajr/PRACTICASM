from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Admin

admin.site.register(Client)

admin.site.register(Admin)

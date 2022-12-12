from django.contrib import admin

# Register your models here.
from .models import User2 as  User

admin.site.register(User)
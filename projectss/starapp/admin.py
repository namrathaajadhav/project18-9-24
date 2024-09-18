from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)  # Display the username in the admin list view

admin.site.register(User, UserAdmin)

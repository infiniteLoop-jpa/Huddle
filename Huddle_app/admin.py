from django.contrib import admin
from .models import Account, Task


# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username']
    search_fields = ['first_name', 'last_name', 'email', 'username']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'people_assigned', 'deadline']
    search_fields = ['name', 'description', 'people_assigned']

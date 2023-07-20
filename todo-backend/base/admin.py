from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo', 'completed',"date_created"]

admin.site.register(Todo, TodoAdmin)
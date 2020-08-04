from django.apps import AppConfig
from django.contrib import admin

from webapp.models import Status, Task_type, Task


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']

class Task_typeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']

admin.site.register(Status, StatusAdmin)
admin.site.register(Task_type, Task_typeAdmin)
admin.site.register(Task)
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ['des_id', 'des_name', 'des_password', 'description', 'mark', 'created_at', ]
    search_fields = ['des_id', 'des_name', 'des_password', 'description', 'mark', 'created_at', ]
    list_filter = ['des_id', 'des_name', 'des_password', 'description', 'mark', 'created_at', ]
    ordering = ['-created_at', ]
    fields = ['des_id', 'des_name', 'des_password', 'description', 'mark', 'created_at', ]
    readonly_fields = ['des_id', 'created_at', ]

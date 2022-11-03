from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['wrk_id', 'wrk_name', 'description', 'mark', 'created_id', 'created_at', ]
    search_fields = ['wrk_id', 'wrk_name', 'description', 'mark', 'created_id', 'created_at', ]
    list_filter = ['wrk_id', 'wrk_name', 'description', 'mark', 'created_id', 'created_at', ]
    ordering = ['-created_at', ]
    fields = ['wrk_id', 'wrk_name', 'description', 'mark', 'created_id', 'created_at', ]
    readonly_fields = ['wrk_id', 'created_at', ]
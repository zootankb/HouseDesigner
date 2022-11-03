from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


@admin.register(ReleaseCopyRight)
class ReleaseCopyRightAdmin(admin.ModelAdmin):
    list_display = ['rcp_id', 'rcp_name', 'rcp_content', 'description', 'mark', 'updated_at', 'created_at', ]
    search_fields = ['rcp_id', 'rcp_name', 'rcp_content', 'description', 'mark', 'updated_at', 'created_at', ]
    list_filter = ['rcp_id', 'rcp_name', 'rcp_content', 'description', 'mark', 'updated_at', 'created_at', ]
    ordering = ['-updated_at', '-created_at', ]
    fields = ['rcp_id', 'rcp_name', 'rcp_content', 'description', 'mark', 'updated_at', 'created_at', ]
    readonly_fields = ['rcp_id', 'updated_at', 'created_at', ]


@admin.register(AssetBundles)
class AssetBundlesAdmin(admin.ModelAdmin):
    list_display = ['ab_id', 'ab_name', 'ab_md5', 'ab_cp', 'description', 'mark', 'updated_at', 'created_at', ]
    search_fields = ['ab_id', 'ab_name', 'ab_md5', 'ab_cp', 'description', 'mark', 'updated_at', 'created_at', ]
    list_filter = ['ab_id', 'ab_name', 'ab_md5', 'ab_cp', 'description', 'mark', 'updated_at', 'created_at', ]
    ordering = ['-updated_at', '-created_at', ]
    fields = ['ab_id', 'ab_name', 'ab_md5', 'ab_cp', 'description', 'mark', 'updated_at', 'created_at', ]
    readonly_fields = ['ab_id', 'updated_at', 'created_at', ]
from django.contrib import admin

from .models import MissionStatement, AppsDescriptions, Summary
# Register your models here.

class MissionStatementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["mission_statement"]}),
        ("Active", {"fields": ["active"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["mission_statement", "pub_date", "was_published_recently", "active"]
    list_filter = ["pub_date", "active"]
    search_fields = ["mission_statement"]


class AppsDescriptionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["app_image"]}),
        (None, {"fields": ["app_name"]}),
        (None, {"fields": ["app_description"]}),
        (None, {"fields": ["app_category"]}),
        ("Active", {"fields": ["active"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["app_name", "app_description", "app_category", "pub_date", "was_published_recently", "active"]    
    list_filter = ["pub_date", "active", "app_category"]
    search_fields = ["app_name"]


class SummaryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["summary"]}),
        ("Active", {"fields": ["active"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["summary", "pub_date", "was_published_recently", "active"]
    list_filter = ["pub_date", "active"]
    search_fields = ["summary"]


admin.site.register(MissionStatement, MissionStatementAdmin)
admin.site.register(AppsDescriptions, AppsDescriptionsAdmin)
admin.site.register(Summary, SummaryAdmin)
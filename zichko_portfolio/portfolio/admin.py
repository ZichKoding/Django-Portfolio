from django.contrib import admin

from .models import MissionStatement, Categories, AppsDescriptions, Summary
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


class CategoriesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["category"]}),
    ]
    list_display = ["category"]
    search_fields = ["category"]


class AppsDescriptionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["app_image", "app_name", "app_description"]}),
        ("Categories", {"fields": ["app_categories"]}),
        ("Active", {"fields": ["active"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

    filter_horizontal = ["app_categories"]
    list_display = ["app_name", "app_description", "pub_date", "was_published_recently", "active"]
    list_filter = ["pub_date", "active"]
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
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(AppsDescriptions, AppsDescriptionsAdmin)
admin.site.register(Summary, SummaryAdmin)
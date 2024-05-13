from django.shortcuts import render

from portfolio.models import AppsDescriptions


class SearchBarView():
    def search_bar():
        pass

    def search_by_name(request):
        pass

    def search_by_category(request):
        pass

    def search_by_description(request):
        pass


class FitlerBoxView():
    def filter_box():
        pass

    def filter_by_category(request):
        pass

    def filter_by_publish_date(request):
        pass

    def filter_by_publish_date_range(request):
        pass


class AppsView():
    def get_apps():
        pass

    def get_seven_most_recent_active_apps():
        pass

    def get_pagination_of_apps():
        pass
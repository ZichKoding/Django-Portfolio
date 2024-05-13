import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .views import SearchBarView, FitlerBoxView, AppsView

# SearchBarView tests
class SearchBarViewTests(TestCase):
    def test_search_bar(self):
        pass

    def test_search_by_name(self):
        pass

    def test_search_by_category(self):
        pass

    def test_search_by_description(self):
        pass


# FitlerBoxView tests
class FitlerBoxViewTests(TestCase):
    def test_filter_box(self):
        pass

    def test_filter_by_category(self):
        pass

    def test_filter_by_publish_date(self):
        pass

    def test_filter_by_publish_date_range(self):
        pass


# AppsView tests
class AppsViewTests(TestCase):
    def test_get_apps(self):
        pass

    def test_get_seven_most_recent_active_apps(self):
        pass

    def test_get_pagination_of_apps(self):
        pass
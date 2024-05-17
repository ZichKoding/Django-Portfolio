import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from portfolio.models import AppsDescriptions
from .views import AppsView

# Need to make an dictionary of data for various test cases. 
# get_default_apps dataset
less_than_seven_apps = [
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "Test App 1",
        "app_description": "Less than seven apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now(),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "Test App 2",
        "app_description": "Less than seven apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=1),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "Test App 3",
        "app_description": "Less than seven apps",
        "app_category": "Test Category 2",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=2),
        "active": False
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "Test App 4",
        "app_description": "Less than seven apps",
        "app_category": "Test Category 2",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=3),
        "active": True
    }
]

more_apps = [
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "More Apps 5",
        "app_description": "More apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=4),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "More Apps 6",
        "app_description": "More apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=5),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "More Apps 7",
        "app_description": "More apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=6),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "More Apps 8",
        "app_description": "More apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=7),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "More Apps 9",
        "app_description": "More apps",
        "app_category": "Test Category 1",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=8),
        "active": True
    },
    {
        "app_image": "images/less_than_seven_apps.png",
        "app_name": "More Apps 10",
        "app_description": "More apps",
        "app_category": "Test Category",
        "app_url": "https://zichkoding.com",
        "app_gh_url": "https://github.com/ZichKoding",
        "pub_date": timezone.now() + datetime.timedelta(days=9),
        "active": True
    }
]

# Need to create a function that will apply the data to the 
# testing database. 

# AppsView tests
class AppsViewTests(TestCase):
    def test_get_default_apps_success(self):
        pass

    def test_search_by_character_success(self):
        pass

    def test_filter_by_category_success(self):
        pass

    def test_coordinator_first_page_success(self):
        pass
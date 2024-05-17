import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from portfolio.models import AppsDescriptions
from .views import AppsView

# Need to make an dictionary of data for various test cases. 
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
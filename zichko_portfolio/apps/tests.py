import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from portfolio.models import AppsDescriptions
from .views import SearchBarView, FitlerBoxView, AppsView


# function for adding test data
def add_test_data_for_searchbar_and_filterbar():
    test_app_1 = {
        "app_name": "Test App 1",
        "app_category": "Test Category 1",
        "app_description": "Test Description 1",
        "app_image": "Test Image 1",
        "pub_date": timezone.now(),
        "active": True,
    }

    test_app_2 = {
        "app_name": "Test App 2",
        "app_category": "Test Category 2",
        "app_description": "Test Description 2",
        "app_image": "Test Image 2",
        "pub_date": timezone.now(),
        "active": True,
    }

    test_app_3 = {
        "app_name": "App 3",
        "app_category": "Category 3",
        "app_description": "Description 3",
        "app_image": "Image 3",
        "pub_date": timezone.now(),
        "active": True,
    }

    test_app_4 = {
        "app_name": "Test App 4",
        "app_category": "Category 4",
        "app_description": "Description 4",
        "app_image": "Image 4",
        "pub_date": timezone.now(),
        "active": False,
    }

    test_app_5 = {
        "app_name": "App 5",
        "app_category": "Test Category 5",
        "app_description": "Description 5",
        "app_image": "Image 5",
        "pub_date": timezone.now(),
        "active": False,
    }

    test_app_6 = {
        "app_name": "App 6",
        "app_category": "Test Category 6",
        "app_description": "Description 6",
        "app_image": "Image 6",
        "pub_date": timezone.now(),
        "active": True,
    }

    # Send the test data to the database
    AppsDescriptions.objects.create(**test_app_1)
    AppsDescriptions.objects.create(**test_app_2)
    AppsDescriptions.objects.create(**test_app_3)
    AppsDescriptions.objects.create(**test_app_4)
    AppsDescriptions.objects.create(**test_app_5)
    AppsDescriptions.objects.create(**test_app_6)
    # Return the test data
    return AppsDescriptions.objects.all()


# SearchBarView tests
class SearchBarViewTests(TestCase):
    def test_search_by_name(self):
        '''
        search_by_name() returns a list of apps whose 
        names contain the characters in the search query.
        '''
        # Create a search query
        search_query = "test"
        # call the add_test_data_for_searchbar_and_filterbar() function
        add_test_data_for_searchbar_and_filterbar()
        # Create a list of expected results
        expected_results = [
            {"app_name": "Test App 1"},
            {"app_name": "Test App 2"}
        ]
        # Call the search_by_name() method
        results = SearchBarView.search_by_name(search_query)
        # Compare the results to the expected results
        self.assertEqual(results, expected_results)

    def test_search_by_category(self):
        '''
        search_by_category() returns a list of apps whose
        categories contain the characters in the search query.
        '''
        # Create a search query
        search_query = "test"
        # call the add_test_data_for_searchbar_and_filterbar() function
        add_test_data_for_searchbar_and_filterbar()
        # Create a list of expected results
        expected_results =[
            {"app_name": "Test App 1"},
            {"app_name": "Test App 2"},
            {"app_name": "App 6"},
        ]
        # Call the search_by_category() method
        results = SearchBarView.search_by_category(search_query)
        # Compare the results to the expected results
        self.assertEqual(results, expected_results)

# FitlerBoxView tests
# class FitlerBoxViewTests(TestCase):
#     def test_filter_box(self):
#         pass

#     def test_filter_by_category(self):
#         pass

#     def test_filter_by_publish_date(self):
#         pass

#     def test_filter_by_publish_date_range(self):
#         pass


# # AppsView tests
# class AppsViewTests(TestCase):
#     def test_get_apps(self):
#         pass

#     def test_get_seven_most_recent_active_apps(self):
#         pass

#     def test_get_pagination_of_apps(self):
#         pass
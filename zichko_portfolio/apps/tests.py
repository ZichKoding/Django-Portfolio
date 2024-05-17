import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from portfolio.models import AppsDescriptions
from .views import AppsView

# Need to make an dictionary of data for various test cases. 
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
def create_apps(apps):
    for app in apps:
        AppsDescriptions.objects.create(
            app_image=app["app_image"],
            app_name=app["app_name"],
            app_description=app["app_description"],
            app_category=app["app_category"],
            app_url=app["app_url"],
            app_gh_url=app["app_gh_url"],
            pub_date=app["pub_date"],
            active=app["active"]
        )


# AppsView tests
class AppsViewTests(TestCase):
    def test_get_default_apps_success(self):
        '''
        Testing the get_default_apps() method to make 
        sure that it will return the 7 most recent active apps 
        along with the pagination information. 
        Expected return is a dictionary with three keys:
        {
            "apps_description": all of the app information of the current page,
            "current_page": this is a numeric value, and by default the value is one,
            "total_pages": the length of pages that holds at least 7 apps per page
        }
        '''
        create_apps(less_than_seven_apps)
        create_apps(more_apps)
        apps_view = AppsView()
        response = apps_view.get_default_apps()
        self.assertEqual(len(response["apps_description"]), 7)
        self.assertEqual(response["apps_description"][0].app_name, "Test App 1")
        self.assertEqual(response["apps_description"][6].app_name, "More Apps 8")
        self.assertEqual(response["current_page"], 1)
        self.assertEqual(response["total_pages"], 2)

    def test_get_default_apps_success_less_than_seven(self):
        '''
        Testing the get_default_apps() method will return at
        least one app when there are less than 7 apps in the database. 
        Expected return is a dictionary with three keys:
        {
            "apps_description": all of the app information of the current page,
            "current_page": this is a numeric value, and by default the value is one,
            "total_pages": the length of pages that holds at least 7 apps per page
        }
        '''
        create_apps(less_than_seven_apps)
        apps_view = AppsView()
        response = apps_view.get_default_apps()
        self.assertEqual(len(response["apps_description"]), 3)
        self.assertEqual(response["apps_description"][0].app_name, "Test App 1")
        self.assertEqual(response["apps_description"][-1].app_name, "Test App 4")
        self.assertEqual(response["current_page"], 1)
        self.assertEqual(response["total_pages"], 1)

    def test_get_default_apps_success_different_page(self):
        '''
        Testing the get_default_apps() method to make 
        sure that it will return the 7 most recent active apps 
        along with the pagination information. 
        Expected return is a dictionary with three keys:
        {
            "apps_description": all of the app information of the current page,
            "current_page": this is a numeric value, and by default the value is one,
            "total_pages": the length of pages that holds at least 7 apps per page
        }
        '''
        create_apps(less_than_seven_apps)
        create_apps(more_apps)
        apps_view = AppsView()
        response = apps_view.get_default_apps(page_number=2)
        self.assertEqual(len(response["apps_description"]), 2)
        self.assertEqual(response["apps_description"][0].app_name, "More Apps 9")
        self.assertEqual(response["apps_description"][6].app_name, "More Apps 10")
        self.assertEqual(response["current_page"], 2)
        self.assertEqual(response["total_pages"], 2)

    def test_get_default_apps_success_no_apps(self):
        '''
        Testing the get_default_apps() method to make
        sure that it will return a list of a default image and message
        when there are no active apps in the database, or 
        upon a database error.
        Expected return is a dictionary with three keys:
        {
            "apps_description": [{
                "app_image": "images/default_image.png",
                "app_name": "No apps found",
                "app_description": "No apps found at this time. Please check back later.",
                "app_category": "No category found",
                "app_url": "https://zichkoding.com",
                "app_gh_url": "https://github.com/ZichKoding",
                "pub_date": timezone.now(),
                "active": True
            }]
            "current_page": this is a numeric value, and by default the value is one,
            "total_pages": the length of pages that holds at least 7 apps per page
        }
        '''
        apps_view = AppsView()
        response = apps_view.get_default_apps()
        self.assertEqual(len(response["apps_description"]), 1)
        self.assertEqual(response["apps_description"][0].app_name, "No apps found at this time. Please check back later.")
        self.assertEqual(response["current_page"], 1)
        self.assertEqual(response["total_pages"], 1)

    def test_search_by_character_success(self):
        pass

    def test_filter_by_category_success(self):
        pass

    def test_coordinator_first_page_success(self):
        pass
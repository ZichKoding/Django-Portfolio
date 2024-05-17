import datetime

from django.utils import timezone
from django.shortcuts import render

from portfolio.models import AppsDescriptions


class AppsView():
    def __init__(self):
        self.default_response = [{
            "app_image": "images/default_image.png",
            "app_name": "No apps found",
            "app_description": "No apps found at this time. Please check back later.",
            "app_category": "No category found",
            "app_url": "https://zichkoding.com",
            "app_gh_url": "https://github.com/ZichKoding",
            "pub_date": timezone.now(),
            "active": True
        }]

    def get_default_apps(self, page_number=1):
        '''
        This method will return, at most, the seven 
        most recent apps from the database. Also, it will
        return the pagination information.
        :param page_number: the current page number
        :return: a dictionary with three keys: {
            "apps_description": all of the app information of the current page,
            "current_page": this is a numeric value, and by default the value is one,
            "total_pages": the length of pages that holds at least 7 apps per page
        }
        '''
        # Get the range of apps to display
        if page_number > 1:
            range_start = (page_number - 1) * 7
            range_end = page_number * 7
        else:
            range_start = 0
            range_end = 7

        # Get the apps or return default message if no apps are found
        try:
            # Get the total number of apps
            total_apps = AppsDescriptions.objects.filter(active=True).count()
            apps = AppsDescriptions.objects.filter(active=True).order_by("pub_date")[range_start:range_end]
            if apps.count() == 0:
                raise AppsDescriptions.DoesNotExist
        except AppsDescriptions.DoesNotExist:
            app_description = self.default_response
            return {
                "apps_description": app_description,
                "current_page": 1,
                "total_pages": 1,
            }
        
        # Create an array of objects with app information
        array_of_apps = list(apps.values())

        # Get the current page and total pages
        current_page = page_number
        total_pages = total_apps // 7 + (total_apps % 7 > 0)

        return {
            "apps_description": array_of_apps,
            "current_page": current_page,
            "total_pages": total_pages,
        }

    def search_by_character(self, characters, page_number=1):
        '''
        This function needs to query the database based on characters
        being searched and return the seven most recent based on characters
        in search criteria. Also, needs to return the pagination information. 
        For example, object is returned with three keys:
        apps_description - all of the app information of the current page
        current_page - this is a numeric value, and by default the value is one. 
        total_pages - the length of pages that holds at least 7 apps per page. 
        '''
        # Get the characters to search for in lowercase
        lowercase_characters = characters.lower()
        # Get the range of apps to display
        if page_number > 1:
            range_start = (page_number - 1) * 7
            range_end = page_number * 7
        else:
            range_start = 0
            range_end = 7
        
        # Get the apps or return default message if no apps are found
        try:
            # Get the total number of apps
            total_apps = AppsDescriptions.objects.filter(app_name__icontains=lowercase_characters, active=True).count()
            apps = AppsDescriptions.objects.filter(app_name__icontains=lowercase_characters, active=True).order_by("pub_date")[range_start:range_end]
            if apps.count() == 0:
                raise AppsDescriptions.DoesNotExist
        except AppsDescriptions.DoesNotExist:
            return {
                "apps_description": self.default_response,
                "current_page": 1,
                "total_pages": 1,
            }
        
        # Create an array of objects with app information
        array_of_apps = list(apps.values())

        # Get the current page and total pages
        current_page = page_number
        total_pages = total_apps // 7 + (total_apps % 7 > 0)

        return {
            "apps_description": array_of_apps,
            "current_page": current_page,
            "total_pages": total_pages,
        }

    def filter_by_category(self, category, page_number=1):
        '''
        This function needs to query the database based on the category.
        It needs to return a list of, at least, the 7 most recent apps 
        from that category. Also, it needs to return the pagination.
        For example, object is returned with three keys:
        apps_description - all of the app information of the current page
        current_page - this is a numeric value, and by default the value is one. 
        total_pages - the length of pages that holds at least 7 apps per page. 
        '''
        return {
            "apps_description": [],  # Replace with actual apps descriptions
            "current_page": 1,  # Replace with actual current page
            "total_pages": 1,  # Replace with actual total pages
        }

    def coordinator(self, url_params):
        '''
        This function will take the request url to splice, split, and parse 
        the data to find the params. If there is no query param found (search or filter)
        then extract the page number from the page_number query. Then call 
        the method, get_default_apps() and return the response. 

        If the query parameters contain search, extract the characters and 
        page_number values, and call the method, search_by_character(), with the query
        parameters and return the response. 

        If the query parameters contain filter, extract the category and 
        page_number values, and call the filter_by_category() with the 
        query parameters. Then return the response. 
        '''
        return {
            "apps_description": [],  # Replace with actual apps descriptions
            "current_page": 1,  # Replace with actual current page
            "total_pages": 1,  # Replace with actual total pages
        }


    
def index(request):
    return render(request, "apps/index.html")
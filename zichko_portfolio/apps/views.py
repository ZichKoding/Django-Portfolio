from django.shortcuts import render

from portfolio.models import AppsDescriptions


class AppsView():
    def get_default_apps(self, page_number=1):
        '''
        This function needs to get the seven most recent apps. 
        It, also, needs to return the pagination information with at 
        7 apps per page. For example, object is returned with three keys:
        apps_description - all of the app information of the current page
        current_page - this is a numeric value, and by default the value is one. 
        total_pages - the length of pages that holds at least 7 apps per page. 
        '''
        pass

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
        pass

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
        pass

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

    
def index(request):
    return render(request, "apps/index.html")
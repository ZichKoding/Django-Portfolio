from django.shortcuts import render

from portfolio.models import AppsDescriptions

def get_apps_descriptions(category=None, page_number=1):
    pass

def index(request):
    return render(request, "apps/index.html")
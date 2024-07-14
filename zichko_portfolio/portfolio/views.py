from django.shortcuts import render

from .models import MissionStatement, AppsDescriptions, Summary


def get_random_mission_statement():
    """
        Return a random mission statement.
    """
    mission_statement = MissionStatement.objects.filter(active=True).order_by("?").first()
    if mission_statement is None:
        return "Software Engineer | Your Vision. My Expertise. Together, we build success."
    return mission_statement

def get_active_summary():
    """
        Return the active summary.
    """
    summary = Summary.objects.filter(active=True).first()
    if summary is None:
        return "Software Engineer with a passion for crafting innovative solutions across web development, data engineering, and emerging technologies. I thrive in building user-centric applications using Django and other modern frameworks. My expertise spans full-stack development, data pipelines, and cloud platforms (AWS). Currently exploring the exciting world of AI, robotics, and Single Board Computers (Raspberry Pi & Arduino)."
    return summary
    
def get_random_active_apps_descriptions():
    """
        Return, at most, 3 random active apps and descriptions.
    """
    apps_description = AppsDescriptions.objects.filter(active=True).order_by("?")[:3]
    if not apps_description:
        return "Featured apps coming soon!"
    return apps_description

def index(request):
    """
        Return the index page.
    """
    mission_statement = get_random_mission_statement()
    summary = get_active_summary()
    app_description = get_random_active_apps_descriptions()
    context = {
        "mission_statement": mission_statement,
        "summary": summary,
        "app_description": app_description,
    }
    return render(request, "portfolio/index.html", context)
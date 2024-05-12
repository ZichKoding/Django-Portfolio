import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Mission Statement model
class MissionStatement(models.Model):
    mission_statement = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.mission_statement
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

# Apps | Descriptions model
class AppsDescriptions(models.Model):
    app_image = models.ImageField(upload_to="images/")
    app_name = models.CharField(max_length=200)
    app_description = models.CharField(max_length=200)
    app_category = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=False)
    # For the Apps app to use:
    # Need to add URL field for each app
    # Need to add GH/Project URL field for each app

    def __str__(self):
        return self.app_name
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

# Summary model
class Summary(models.Model):
    summary = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.summary
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
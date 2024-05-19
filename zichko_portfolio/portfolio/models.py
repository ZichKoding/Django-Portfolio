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
    

# Categories model
class Categories(models.Model):
    category = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category
    

# Apps | Descriptions model
class AppsDescriptions(models.Model):
    app_image = models.ImageField(upload_to="images/")
    app_name = models.CharField(max_length=200)
    app_description = models.CharField(max_length=200)
    app_categories = models.ManyToManyField(Categories)
    app_url = models.URLField(max_length=200, default="https://zichkoding.com")
    app_gh_url = models.URLField(max_length=200, default="https://github.com/ZichKoding")
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=False)

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
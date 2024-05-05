import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import MissionStatement, AppsDescriptions, Summary


# Mission Statement model tests
class MissionStatementModelTests(TestCase):
    def test_was_published_recently_with_old_mission(self):
        """
        was_published_recently() returns False for mission statements whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_mission = MissionStatement(pub_date=time)
        self.assertIs(old_mission.was_published_recently(), False)

    def test_was_published_recently_with_recent_mission(self):
        """
        was_published_recently() returns True for mission statements whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_mission = MissionStatement(pub_date=time)
        self.assertIs(recent_mission.was_published_recently(), True)

    def test_was_published_recently_with_future_mission(self):
        """
        was_published_recently() returns False for mission statements whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_mission = MissionStatement(pub_date=time)
        self.assertIs(future_mission.was_published_recently(), False)


# Apps | Descriptions model tests
class AppsDescriptionsModelTests(TestCase):
    def test_was_published_recently_with_old_app(self):
        """
        was_published_recently() returns False for apps whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_app = AppsDescriptions(pub_date=time)
        self.assertIs(old_app.was_published_recently(), False)

    def test_was_published_recently_with_recent_app(self):
        """
        was_published_recently() returns True for apps whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_app = AppsDescriptions(pub_date=time)
        self.assertIs(recent_app.was_published_recently(), True)

    def test_was_published_recently_with_future_app(self):
        """
        was_published_recently() returns False for apps whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_app = AppsDescriptions(pub_date=time)
        self.assertIs(future_app.was_published_recently(), False)


# Summary model tests
class SummmaryTests(TestCase):
    def test_was_published_recently_with_old_summary(self):
        """
        was_published_recently() returns False for summaries whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_summary = Summary(pub_date=time)
        self.assertIs(old_summary.was_published_recently(), False)

    def test_was_published_recently_with_recent_summary(self):
        """
        was_published_recently() returns True for summaries whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_summary = Summary(pub_date=time)
        self.assertIs(recent_summary.was_published_recently(), True)

    def test_was_published_recently_with_future_summary(self):
        """
        was_published_recently() returns False for summaries whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_summary = Summary(pub_date=time)
        self.assertIs(future_summary.was_published_recently(), False)
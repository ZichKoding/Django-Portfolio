import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import MissionStatement, AppsDescriptions, Summary
from .views import get_random_mission_statement, get_active_summary, get_random_active_apps_descriptions

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


# Mission Statement view tests
class MissionStatementViewTests(TestCase):
    def test_get_mission_statement_fail(self):
        """
        get_mission_statement() returns the default mission statement when no mission statements exist.
        """
        mission_statement = get_random_mission_statement()
        self.assertEqual(mission_statement, "Software Engineer | Your Vision. My Expertise. Together, we build success.")

    def test_get_mission_statement(self):
        """
        get_mission_statement() returns the default mission statement when no mission statements exist.
        """
        MissionStatement.objects.create(mission_statement="Test mission statement", pub_date=timezone.now(), active=True)
        mission_statement = get_random_mission_statement()
        # Check if the mission statement is active
        self.assertTrue(mission_statement.active)
        # Check if the mission statement is correct
        self.assertEqual(mission_statement.mission_statement, "Test mission statement")


# Summary view tests
class SummaryViewTests(TestCase):
    def test_get_summary_fail(self):
        """
        get_summary() returns the default summary when no summaries exist.
        """
        summary = get_active_summary()
        self.assertEqual(summary, "Software Engineer with a passion for crafting innovative solutions across web development, data engineering, and emerging technologies. I thrive in building user-centric applications using Django and other modern frameworks. My expertise spans full-stack development, data pipelines, and cloud platforms (AWS). Currently exploring the exciting world of AI, robotics, and Single Board Computers (Raspberry Pi & Arduino).")

    def test_get_summary(self):
        """
        get_summary() returns the default summary when no summaries exist.
        """
        Summary.objects.create(summary="Test summary", pub_date=timezone.now(), active=True)
        summary = get_active_summary()
        # Check if the summary is active
        self.assertTrue(summary.active)
        # Check if the summary is correct
        self.assertEqual(summary.summary, "Test summary")


# Apps | Descriptions view tests
class AppsDescriptionsViewTests(TestCase):
    def test_get_apps_descriptions_fail(self):
        """
        get_apps_descriptions() returns the default apps descriptions when no apps descriptions exist.
        """
        apps_descriptions = get_random_active_apps_descriptions()
        self.assertEqual(apps_descriptions, "Featured apps coming soon!")

    def test_get_apps_descriptions(self):
        """
        get_apps_descriptions() returns the default apps descriptions when no apps descriptions exist.
        """
        AppsDescriptions.objects.create(app_name="Test app", app_description="Test app description", app_category="Test app category", pub_date=timezone.now(), active=True)
        apps_descriptions = get_random_active_apps_descriptions()
        # Check if there is at least 3 apps descriptions
        self.assertTrue(len(apps_descriptions) <= 3)
        # Check if all apps descriptions are active
        for apps_description in apps_descriptions:
            self.assertTrue(apps_description.active)
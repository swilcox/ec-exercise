"""functional tests"""
from django.test import TestCase
from changelog.models import ChangeLog
from samples.models import User, Organization


class FunctionalChangeLogTest(TestCase):
    def test_changelog_exercise(self):
        """test based on the exercise example"""

        user = User(first_name="x")
        user.save()
        user.last_name = "y"
        user.email = "x@email.com"
        user.save()
        org = Organization(name="A", slug="a")
        org.save()
        org.name = "B"
        org.save()
        user.delete()
        self.assertEqual(ChangeLog.objects.count(), 5)
        self.assertEqual(
            ChangeLog.objects.all()[0].to_json_str(),
            '{"operation": "created", "changed": ["id", "first_name"], "data": {"id": 1, "first_name": "x"}, "pk": 1, "class": "User", "time": "%s"}'
            % ChangeLog.objects.all()[0].ts.isoformat(),
        )
        self.assertEqual(
            ChangeLog.objects.all()[1].to_json_str(),
            '{"operation": "updated", "changed": ["last_name", "email"], "data": {"last_name": "y", "email": "x@email.com"}, "pk": 1, "class": "User", "time": "%s"}'
            % ChangeLog.objects.all()[1].ts.isoformat(),
        )
        self.assertEqual(
            ChangeLog.objects.all()[2].to_json_str(),
            '{"operation": "created", "changed": ["id", "name", "slug"], "data": {"id": 1, "name": "A", "slug": "a"}, "pk": 1, "class": "Organization", "time": "%s"}'
            % ChangeLog.objects.all()[2].ts.isoformat(),
        )
        self.assertEqual(
            ChangeLog.objects.all()[3].to_json_str(),
            '{"operation": "updated", "changed": ["name"], "data": {"name": "B"}, "pk": 1, "class": "Organization", "time": "%s"}'
            % ChangeLog.objects.all()[3].ts.isoformat(),
        )
        self.assertEqual(
            ChangeLog.objects.all()[4].to_json_str(),
            '{"operation": "deleted", "changed": null, "data": null, "pk": 1, "class": "User", "time": "%s"}'
            % ChangeLog.objects.all()[4].ts.isoformat(),
        )

"""
Tests for models (samples app)
"""

from django.test import TestCase
from ..models import User, Organization


class TestUserModel(TestCase):
    """Test the User Model"""

    def test_user_model_str(self):
        """test user model __str__ method"""
        u1 = User.objects.create(
            first_name="Emmett", last_name="Brown", email="doc.brown@example.com"
        )
        self.assertEqual(str(u1), "Emmett Brown (doc.brown@example.com)")


class TestOrganizationModel(TestCase):
    """Test the Organization Model"""

    def test_organization_model_str(self):
        o1 = Organization.objects.create(
            name="Hill Valley Preservation Society", slug="hill-valley-ps"
        )
        self.assertEqual(str(o1), "Hill Valley Preservation Society (hill-valley-ps)")

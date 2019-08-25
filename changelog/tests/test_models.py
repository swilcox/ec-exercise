"""Model tests for changelog"""
import json
from django.test import TestCase
from ..models import ChangeLog


class TestChangeLogModel(TestCase):
    """Test the ChangeLog Model"""

    def test_str(self):
        """test __str__ of ChangeLog"""
        u1 = ChangeLog.objects.create(
            operation='created',
            data=json.dumps({'id': 1, 'name': 'Testing'}),
            pk_value=1,
            class_short_name='MyModel',
            label_name='testing.MyModel',
        )
        ts_str = u1.ts.isoformat()
        self.assertEqual(
            str(u1),
            '{"operation": "created", "changed": ["id", "name"], "data": {"id": 1, "name": "Testing"}, "pk": 1, "class": "MyModel", "time": "%s"}' % ts_str
        )

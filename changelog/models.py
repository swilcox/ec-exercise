"""
changelog models
"""

import json
from django.db import models


class ChangeLog(models.Model):
    """ChangeLog Model for the actual changes we record"""
    ts = models.DateTimeField(db_index=True, auto_now_add=True)
    operation = models.CharField(max_length=20, choices=(('created', 'created'), ('updated', 'updated'), ('deleted', 'deleted')))
    label_name = models.CharField(max_length=255)
    class_short_name = models.CharField(max_length=255)
    pk_value = models.BigIntegerField()
    data = models.TextField(blank=True, null=True, default=None)
    
    def to_json_str(self):
        data = json.loads(self.data) if self.data else None
        return json.dumps(
            {
                "operation": self.operation,
                "changed": list(data.keys()) if data else None,
                "data": data,
                "pk": self.pk_value,
                "class": self.class_short_name,
                "time": self.ts.isoformat(),
            }
        )

    def __str__(self):
        return self.to_json_str()

"""
Sample Models to demo the tracker
"""
from django.db import models


class User(models.Model):
    """Sample User model for demo'ing our tracker"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Organization(models.Model):
    """Sample Organization model for demo'ing our tracker"""
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name} ({self.slug})"

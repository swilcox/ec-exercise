"""
signals.py

Define signals for our changelog purposes
"""

import json

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
import pytz
from .models import ChangeLog


@receiver(pre_save)
def pre_save_handler(sender, **kwargs):
    """handle signals prior to final save"""
    if sender._meta.label in settings.TRACKED_MODELS:
        instance = kwargs.get('instance')
        original = sender.objects.filter(pk=instance.pk).first() if instance and instance.pk else None
        if original:        # only deal with "updates"
            instance_dict = {field.name: getattr(instance, field.name) for field in instance._meta.fields}
            data = {field: value for field, value in instance_dict.items() if getattr(original, field) != value}
            ChangeLog.objects.create(
                operation="updated",
                data=json.dumps(data),
                pk_value=instance.pk,
                class_short_name=sender._meta.object_name,
                label_name=sender._meta.label,
            )


@receiver(post_save)
def post_save_handler(sender, **kwargs):
    """handle signals after save"""
    if sender._meta.label in settings.TRACKED_MODELS:
        if kwargs.get('created'):       # only deal with newly created instances
            instance = kwargs.get('instance')
            full_data = {field.name: getattr(instance, field.name) for field in instance._meta.fields}
            data = {f: v for f, v in full_data.items() if v is not None and str(v) != ''}
            ChangeLog.objects.create(
                operation='created',
                data=json.dumps(data),
                pk_value=instance.pk,
                class_short_name=sender._meta.object_name,
                label_name=sender._meta.label,
            )


@receiver(post_delete)
def post_delete_handler(sender, **kwargs):
    """handler for delete signals""" 
    if sender._meta.label in settings.TRACKED_MODELS:
        instance = kwargs.get('instance')
        ChangeLog.objects.create(
            operation='deleted',
            pk_value=instance.pk,
            class_short_name=sender._meta.object_name,
            label_name=sender._meta.label,
        )

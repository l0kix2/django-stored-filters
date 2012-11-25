# coding: utf-8
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType

from .models import Filter
from .query import filters_as_Q

def create_filter(conditions=None, exclusions=None,
                  model_class=None, app_label=None, model_name=None):
    if model_class:
        content_type = ContentType.objects.get_for_model(model_class)
    elif app_label and model_name:
        content_type = ContentType.objects.get_by_natural_key(
            app_label=app_label, model=model_name)
    else:
        raise Exception(
            'You should specify model_class or app_label and model_name')

    return Filter.objects.create(
        conditions=conditions, exclusions=exclusions, content_type=content_type
    )


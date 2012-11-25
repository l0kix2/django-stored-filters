# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

class Filter(models.Model):
    description = models.CharField(
        verbose_name='short description',
        max_length=255,
        blank=True,
    )
    conditions = JSONField(
        verbose_name='filter conditions',
        blank=True, null=True,
    )
    exclusions = JSONField(
        verbose_name='exclude conditions',
        blank=True, null=True,
    )
    content_type = models.ForeignKey(
        verbose_name='content type',
        to='contenttypes.ContentType',
    )

    def __unicode__(self):
        return "[%s] %s" % (self.content_type, self.description)

# coding: utf-8
from __future__ import unicode_literals

def fetch_lookups(lookups):
    for lookup in lookups:
        yield {'conditions': lookup.conditions,
               'exclusions': lookup.exclusions}

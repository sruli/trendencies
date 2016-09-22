from __future__ import unicode_literals
from django.db import models
from picklefield.fields import PickledObjectField
from django.conf import settings


class Reporter(models.Model):
    name = models.CharField(max_length=100, db_index=True, blank=False, null=False)
    stories_coverage = PickledObjectField()
    stories_trendencies = PickledObjectField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Story(models.Model):
    name = models.CharField(max_length=100, db_index=True, blank=False, null=False)

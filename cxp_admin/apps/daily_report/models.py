# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import mongoengine
# Create your models here.


class DailyReport(mongoengine.Document):
    _id = mongoengine.StringField(max_length=128, required=True)
    task_owner = mongoengine.StringField(max_length=128, required=True)
    task_cost = mongoengine.StringField(max_length=64, required=True)
    task_progress = mongoengine.StringField(max_length=64, required=True)
    task_type = mongoengine.StringField(max_length=64, required=True)
    task_risk = mongoengine.StringField(max_length=64, required=True)
    task_content = mongoengine.StringField(max_length=256, required=True)
    task_date = mongoengine.StringField(max_length=256)

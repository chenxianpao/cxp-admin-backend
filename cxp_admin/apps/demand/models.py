# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import mongoengine
# Create your models here.


class Demand(mongoengine.Document):
    _id = mongoengine.StringField(max_length=128, required=True)
    name = mongoengine.StringField(max_length=128, required=True)
    desc = mongoengine.StringField(max_length=128, required=True)
    version = mongoengine.StringField(max_length=128)
    principal = mongoengine.StringField(max_length=128, required=True)
    task_progress = mongoengine.StringField(max_length=128, required=True)
    task_desc = mongoengine.StringField(max_length=256)
    design_doc = mongoengine.StringField(max_length=128, required=True)
    test_case = mongoengine.StringField(max_length=128, required=True)
    modify_time = mongoengine.StringField(max_length=128, required=True)

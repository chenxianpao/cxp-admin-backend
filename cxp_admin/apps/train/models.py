# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import mongoengine
# Create your models here.


class Train(mongoengine.Document):
    _id = mongoengine.IntField(required=True)
    title = mongoengine.StringField(max_length=128, required=True)
    content = mongoengine.StringField(max_length=256)
    lecturer = mongoengine.StringField(max_length=64, required=True)
    time = mongoengine.StringField(max_length=64, required=True)
    duration = mongoengine.StringField(max_length=64, required=True)
    students = mongoengine.StringField(max_length=256, required=True)
    annex = mongoengine.StringField(max_length=256)

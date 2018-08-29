# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import mongoengine


# Create your models here.
class Machine(mongoengine.Document):
    hostname = mongoengine.StringField(max_length=16)
    ip_address = mongoengine.StringField(max_length=16)
    cluster = mongoengine.StringField(max_length=16)
    use_desc = mongoengine.StringField(max_length=128)

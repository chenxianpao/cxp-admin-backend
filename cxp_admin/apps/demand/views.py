# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Demand

# Create your views here.

"""
_id = mongoengine.StringField(max_length=128, required=True)
name = mongoengine.StringField(max_length=128, required=True)
desc = mongoengine.StringField(max_length=128, required=True)
version = mongoengine.StringField(max_length=128)
principal = mongoengine.StringField(max_length=128, required=True)
task_progress = mongoengine.StringField(max_length=128, required=True)
task_desc = mongoengine.StringField(max_length=256)
design_doc = mongoengine.StringField(max_length=128, required=True)
test_case = mongoengine.StringField(max_length=128, required=True)

"""


def demand(request):
    request.encoding = 'utf-8'
    print(request.method)
    result = ""
    if request.method == 'GET':
        print(request.GET)
        result = list()
        for item in Demand.objects.all():
            result.append({'_id': item._id, 'name': item.name,
                           'desc': item.desc, 'version': item.version,
                           'principal': item.principal, 'task_progress': item.task_progress,
                           'task_desc': item.task_desc,
                           'test_case': item.test_case, 'design_doc': item.design_doc})
    elif request.method == 'POST':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        _id = request_data.get('_id')
        name = request_data.get('name')
        desc = request_data.get('desc')
        version = request_data.get('version')
        principal = request_data.get('principal')
        task_progress = request_data.get('task_progress')
        task_desc = request_data.get('task_desc')
        test_case = request_data.get('test_case')
        design_doc = request_data.get('design_doc')
        Demand.objects.create(_id=_id, name=name, desc=desc, version=version, principal=principal,
                              task_progress=task_progress, task_desc=task_desc, test_case=test_case,
                              design_doc=design_doc)
    elif request.method == 'DELETE':
        print(request.GET)
        _id = request.GET.get('_id')
        Demand.objects.filter(_id=_id).delete()
    elif request.method == 'PUT':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        _id = request_data.get('_id')
        name = request_data.get('name')
        desc = request_data.get('desc')
        version = request_data.get('version')
        principal = request_data.get('principal')
        task_progress = request_data.get('task_progress')
        task_desc = request_data.get('task_desc')
        test_case = request_data.get('test_case')
        design_doc = request_data.get('design_doc')
        Demand.objects.filter(_id=_id).update(name=name, desc=desc, version=version, principal=principal,
                                              task_progress=task_progress, task_desc=task_desc, test_case=test_case,
                                              design_doc=design_doc)
    else:
        print("invalid http method")
    response = HttpResponse(json.dumps(result))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

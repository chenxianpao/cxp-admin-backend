# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyReport
from mongoengine import Q

# Create your views here.
"""
    task_owner = mongoengine.StringField(max_length=128, required=True)
    task_cost = mongoengine.StringField(max_length=64, required=True)
    task_type = mongoengine.StringField(max_length=64, required=True)
    task_risk = mongoengine.StringField(max_length=64, required=True)
    task_content = mongoengine.StringField(max_length=256, required=True)
    task_date = mongoengine.StringField(max_length=256)
"""


def daily_report(request):
    request.encoding = 'utf-8'
    print(request.method)
    result = ""
    if request.method == 'GET':
        print(request.GET)
        user_list = request.GET.getlist('user_list')
        task_date = request.GET.get('task_date')
        print(user_list)
        print(task_date)
        result = list()
        tmp_dict = dict()
        query_set = None
        for user_index in range(len(user_list)):
            if user_index == 0:
                query_set = Q(task_owner=user_list[user_index])
            else:
                query_set |= Q(task_owner=user_list[user_index])
            result.append({'reporter_name': user_list[user_index], 'reporter_data': list()})
            tmp_dict[user_list[user_index]] = list()
        db_result = DailyReport.objects(query_set & Q(task_date=task_date))
        for db_item in db_result:
            # print(type(item))
            tmp_dict[db_item.task_owner].append({'_id': db_item._id, 'task_cost': db_item.task_cost,
                                                 'task_type': db_item.task_type, 'task_risk': db_item.task_risk,
                                                 'task_content': db_item.task_content, 'task_date': db_item.task_date,
                                                 'task_progress': db_item.task_progress})
            # print((db_item.task_owner))

        for user_item in result:
            user_item['reporter_data'] = tmp_dict[user_item['reporter_name']]

        print(result)
    elif request.method == 'POST':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        _id = request_data.get('_id')
        task_owner = request_data.get('task_owner')
        task_cost = request_data.get('task_cost')
        task_type = request_data.get('task_type')
        task_risk = request_data.get('task_risk')
        task_content = request_data.get('task_content')
        task_date = request_data.get('task_date')
        task_progress = request_data.get('task_progress')
        DailyReport.objects.create(_id=_id, task_owner=task_owner, task_cost=task_cost, task_type=task_type,
                                   task_risk=task_risk,
                                   task_content=task_content, task_date=task_date, task_progress=task_progress)
    elif request.method == 'DELETE':
        print(request.GET)
        task_id = request.GET.get('_id')
        DailyReport.objects.filter(_id=task_id).delete()
    elif request.method == 'PUT':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        _id = request_data.get('_id')
        task_owner = request_data.get('task_owner')
        task_cost = request_data.get('task_cost')
        task_type = request_data.get('task_type')
        task_risk = request_data.get('task_risk')
        task_content = request_data.get('task_content')
        task_date = request_data.get('task_date')
        task_progress = request_data.get('task_progress')
        DailyReport.objects.filter(_id=_id).update(task_owner=task_owner, task_cost=task_cost, task_type=task_type,
                                                   task_risk=task_risk,
                                                   task_content=task_content, task_date=task_date,
                                                   task_progress=task_progress)
    else:
        print("invalid http method")
    response = HttpResponse(json.dumps(result))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

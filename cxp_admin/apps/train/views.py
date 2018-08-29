# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Train

# Create your views here.


def train(request):
    request.encoding = 'utf-8'
    print(request.method)
    result = ""
    if request.method == 'GET':
        print(request.GET)
        result = list()
        for item in Train.objects.all():
            result.append({'_id': item._id, 'title': item.title,
                           'content': item.content, 'lecturer': item.lecturer,
                           'time': item.time, 'duration': item.duration, 'students': item.students,
                           'annex': item.annex})
    elif request.method == 'POST':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        _id = request_data.get('_id')
        title = request_data.get('title')
        content = request_data.get('content')
        lecturer = request_data.get('lecturer')
        time = request_data.get('time')
        duration = request_data.get('duration')
        students = request_data.get('students')
        annex = request_data.get('annex')
        Train.objects.create(_id=_id, title=title, content=content, lecturer=lecturer, time=time,
                             duration=duration, students=students, annex=annex)
    elif request.method == 'DELETE':
        print(request.GET)
        _id = request.GET.get('_id')
        Train.objects.filter(_id=_id).delete()
    elif request.method == 'PUT':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        _id = request_data.get('_id')
        title = request_data.get('title')
        content = request_data.get('content')
        lecturer = request_data.get('lecturer')
        time = request_data.get('time')
        duration = request_data.get('duration')
        students = request_data.get('students')
        annex = request_data.get('annex')
        Train.objects.filter(_id=_id).update(title=title, content=content, lecturer=lecturer, time=time,
                                             duration=duration, students=students, annex=annex)
    else:
        print("invalid http method")
    response = HttpResponse(json.dumps(result))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

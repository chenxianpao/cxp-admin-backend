# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Machine
import json


# Create your views here.

def machine(request):
    request.encoding = 'utf-8'
    print(request.method)
    result = ""
    if request.method == 'GET':
        print("getttttttttttt")
        print(request.GET)
        result = list()
        for item in Machine.objects.all():
            result.append({'hostname': item.hostname, 'ip_address': item.ip_address,
                           'cluster': item.cluster, 'use_desc': item.use_desc})
    elif request.method == 'POST':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        hostname = request_data.get('hostname')
        ip_address = request_data.get('ip_address')
        cluster = request_data.get('cluster')
        use_desc = request_data.get('use_desc')
        Machine.objects.create(hostname=hostname, ip_address=ip_address, cluster=cluster, use_desc=use_desc)
    elif request.method == 'DELETE':
        print(request.GET)
        print(dir(request))
        hostname = request.GET.get('hostname')
        print(hostname)
        Machine.objects.filter(hostname=hostname).delete()
    elif request.method == 'PUT':
        print(json.loads(request.body))
        request_data = json.loads(request.body)
        hostname = request_data.get('hostname')
        ip_address = request_data.get('ip_address')
        cluster = request_data.get('cluster')
        use_desc = request_data.get('use_desc')
        Machine.objects.filter(hostname=hostname).update(ip_address=ip_address, cluster=cluster, use_desc=use_desc)
    else:
        print("invalid http method")

    response = HttpResponse(json.dumps(result))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response



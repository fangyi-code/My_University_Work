# 管理员进行客户管理
from typing import Required
from django.http import JsonResponse
from common.models import Customer
import json

def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret':0,'retlist':retlist})

def addcustomer(request):
    info = request.params['data']
    record = Customer.objects.create(name = info['name'],
            phonenumber = info['phonenumber'],
            address = info['address'])

    return JsonResponse({'ret':0,'id':record.id})

def modifycustomer(request):
    customerid = request.params['id']
    newdata = request.params['newdata']

    try:
        customer = Customer.objects.get(id = customerid)
    except Customer.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为"{customerid}"的客户不存在。'})
    
    if 'name' in  newdata:
        customer.name = newdata['name']
    if 'phonenumber' in  newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in  newdata:
        customer.address = newdata['address']
    customer.save()

    return JsonResponse({'ret': 0})

def deletecustomer(request):
    customerid = request.params['id']

    try:
        customer = Customer.objects.get(id = customerid)
    except Customer.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为"{customerid}"的客户不存在。'})
    customer.delete()

    return JsonResponse({'ret':0})

from lib.handler import dispatcherBase

Action2Handler = {
    'list_customer': listcustomers,
    'add_customer': addcustomer,
    'modify_customer': modifycustomer,
    'del_customer': deletecustomer,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)
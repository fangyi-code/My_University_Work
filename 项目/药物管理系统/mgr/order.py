from django.http import JsonResponse
from django.db.models import F
from django.db import IntegrityError, transaction
import traceback

# 导入 Order 对象定义
from  common.models import  Order,OrderMedicine

import json

def addorder(request):
    info = request.params['data']

    with transaction.atomic():
        medicinelist  = info['medicinelist']

        new_order = Order.objects.create(name=info['name'],
            customer_id=info['customerid'],
            # 写入json格式的药品数据到 medicinelist 字段中
            medicinelist=json.dumps(medicinelist,ensure_ascii=False),)

        batch = [OrderMedicine(order_id=new_order.id,
                               medicine_id=medicine['id'],
                               amount=medicine['amount'])
                 for medicine in medicinelist]

        OrderMedicine.objects.bulk_create(batch)

    return JsonResponse({'ret': 0, 'id': new_order.id})

def listorder(request):
    qs = Order.objects \
        .annotate(
                customer_name=F('customer__name')
        )\
        .values(
        'id', 'name', 'create_date',
        'customer_name',
        'medicinelist'
    )

    # 将 QuerySet 对象 转化为 list 类型
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def deleteorder(request):
    # 获取订单ID
    oid = request.params['id']

    try:

        one = Order.objects.get(id=oid)
        with transaction.atomic():

            # 一定要先删除 OrderMedicine 里面的记录
            OrderMedicine.objects.filter(order_id=oid).delete()
            # 再删除订单记录
            one.delete()

        return JsonResponse({'ret': 0, 'id': oid})

    except Order.DoesNotExist:
        return JsonResponse({
            'ret': 1,
            'msg': f'id 为`{oid}`的订单不存在'
        })

    except:
        err = traceback.format_exc()
        return JsonResponse({'ret': 1, 'msg': err})

from lib.handler import dispatcherBase

Action2Handler = {
    'list_customer': listorder,
    'add_customer': addorder,
    'delete_customer': deleteorder
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)
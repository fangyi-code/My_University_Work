from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
    #客户名称
    name = models.CharField(max_length = 200)

    #联系电话
    phonenumber = models.CharField(max_length = 200)

    #地址
    address = models.CharField(max_length = 200)


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    sn = models.CharField(max_length=200)
    desc = models.CharField(max_length = 200)

class Order(models.Model):
    name = models.CharField(max_length=200,null = True,blank = True)
    create_date = models.DateTimeField(default=datetime.datetime.now)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    medicines = models.ManyToManyField(Medicine,through = 'OrderMedicine')
    medicinelist =  models.CharField(max_length=2000,null=True,blank=True)

class OrderMedicine(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine,on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()


#################################################
# 国家表
class Country(models.Model):
    name = models.CharField(max_length=100)

# 学生表， country 字段是国家表的外键，形成一对多的关系
class Student(models.Model):
    name    = models.CharField(max_length=100)
    grade   = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country,
                                on_delete=models.PROTECT)

    
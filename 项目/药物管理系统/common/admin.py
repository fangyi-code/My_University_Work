from django.contrib import admin
#.models：相对导入，指向同一目录下的 models.py
from .models import Customer
# Register your models here.
#admin.site：Django 管理后台的全局注册表
admin.site.register(Customer)
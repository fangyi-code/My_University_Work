#string.digit给出0-9的字符串，k=7指定7个，random.choices随机选择
import random
import string
from datetime import datetime
import geocoder

#前面英文指定，后数字用当前日期和random函数生成随机数字。
def id():
    prefix = "NO.HBI"
    date = datetime.now().strftime("%y%m%d")
    # string.digit给出0-9的字符串，k=7指定7个，random.choices随机选择
    # join（）将列表中的字符串连接，可与split连用，‘’表示元素之间不用任何分隔符。
    random_ = ''.join(random.choices(string.digits,k=7))
    return f"{prefix}{date}{random_}",date

date_1 = datetime.now().strftime("%y年%m月%d日")
# 生成地址，需安装geocoder包
geocoder = geocoder.ip('me')
# 使date变为全局变量
tree_id,date_id = id()

name = input("感谢您对环保的贡献！请输入您的名字：")
tree = input("感谢您对环保的贡献！请输入您想种植的树：")

print("         植树证书")
print("--------------------------")
print(f"{name} 谢谢你：")
print(f"    你申请种植的 {tree} ,将由伊利\n公益基金会负责种下。查看种植进程>")
print("\n")
print(f"树苗编号：{tree_id}")
print(f"申请时间：{date_1}")
print(f"种植地点：{geocoder.city}")
print("--------------------------")
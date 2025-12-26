# 物流费用计算
print("这是一个物流费用计算器")
def pay():
    # 输入重量和地区
    kg = float(input("请输入要寄出快递的重量(默认重量单位：kg)："))
    area = input("请输入收货的地区，用编号表示：华东地区为1，华南地区为2，华北地区为3:")
    # 华东
    if area == "1":
        if 0 <= kg <= 2:
            price = kg*13
            return price
        elif 2 < kg:
            price = kg*13 + 3*(kg-2)
            return price

    # 华南
    if area == "2":
        if 0 <= kg <= 2:
            price = kg*12
            return price
        elif 2 < kg:
            price = kg*12 + 2*(kg-2)
            return price
    # 华北
    if area == "3":
        if 0 <= kg <= 2:
            price = kg*14
            return price
        elif 2 < kg:
            price = kg*14 + 4*(kg-2)
            return price


# 循环
while True:
    # 便于输出
    result = pay()
    print(f"您需要支付：{result}元")
    # 循环使用
    print("是否需要开始新一轮计算？如果是，请输入“1”：")
    a = input()
    if a != "1":
        break
name,position,phone,email = 1, 1, 1, 1

def input_data():
    global name,position,phone,email
    # 防止过多或过少输入
    data = input("请输入您的姓名，职位，电话号码和电子邮箱！中间用逗号分隔:\n").split(",")
    # 截取前四个,即列表切片操作
    data = data[:4]
    # 防止数量不够
    while len(data) < 4:
        # data实际上是一个列表
        data.append("")
    name, position, phone, email = data

def print_data():
    # 使用上面修改完后的全局变量
    global name, position, phone, email
    print("=======================================")
    print(f"姓名：{name}")
    print(f"职位：{position}")
    print(f"电话：{phone}")
    print(f"电子邮箱：{email}")
    print("=======================================")
    print("\n")

# 循环部分
while True:
    input_data()
    print_data()
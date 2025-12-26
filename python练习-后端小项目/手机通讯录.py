print("这是一个手机通讯录！")
print("该通讯录共有6个功能:")
print("添加联系人(编号1)")
print("查看通讯录(编号2)")
print("删除联系人(编号3)")
print("修改联系人(编号4)")
print("查找联系人(编号5)")
print("退出(编号6)")

contact = {}
# 菜单
def menu():
    #判断部分
    if input_index == 1:
        index_1()
    elif input_index == 2:
        index_2()
    elif input_index == 3:
        index_3()
    elif input_index == 4:
        index_4()
    elif input_index == 5:
        index_5()
    elif input_index == 6:
        print("您已选择：退出手机通讯录")
        return "exit"
    return True

def index_1():
        while True:
            # strip（）可去除首位空格。一旦只有空格，就会变成空字符串，便于之后验证。
            name = input("请输入姓名！").strip()
            if name:
                break
            print("姓名不能为空，请重新输入！")
        
        while True:
            phone = input("请输入手机号：").strip()
            if phone:
                break
            print("手机号不能为空，请重新输入！")
        
        while True:
            email = input("请输入电子邮箱：").strip()
            if email:
                break
            print("电子邮箱不能为空，请重新输入！")
        
        while True:
            address = input("请输入联系地址：").strip()
            if address:
                break
            print("联系地址不能为空，请重新输入！")
        
        # 嵌套字典，一个键对应多个值
        contact[name] = {
            'phone':phone,
            'email':email,
            'address':address
        }
        print("输入成功！您可以随时进行查看或修改")

def index_2():
    if len(contact) == 0:
        print("通讯录为空，请先添加联系人！")
    else:
        for name,info in contact.items():
            print("="*10)
            print(f"姓名:{name}")
            print(f"手机号:{info['phone']}")
            print(f"电子邮箱:{info['email']}")
            print(f"联系地址:{info['address']}")

def index_3():
    if len(contact) == 0:
            print("通讯录为空，请先添加联系人！")
    else:
        name = input("请输入要删除的联系人姓名：")
        if name in contact:
            del contact[name]
            print("已成功删除！")
        else:
            print("联系人不存在")

def index_4():
    if len(contact) == 0:
        print("通讯录为空，请先添加联系人！")
    else:
        name = input("请输入要修改的联系人姓名：")
        if name in contact:
            info = contact[name]
            old = input("请输入要修改的项目：'phone'/'email'/'address'：")
            update = input("请输入新的信息：")
            info[old] = update
            print("修改成功！")
        else:
            print("联系人不存在")       

def index_5():
    if len(contact) == 0:
        print("通讯录为空，请先添加联系人！")
    else:
        name = input("请输入要查找的姓名：")
        # 查找的是键，如果遍历，找到的也是键
        if name in contact:
            # info是information..
            info = contact[name]
            print(f"手机号：{info['phone']}") # 字典取值！
            print(f"邮箱：{info['email']}")
            print(f"地址：{info['address']}")
        else:
            print("联系人不存在")

# 输入部分
def input_num():
    # 定义全局变量
    global input_index
    while True:
        try:
            input_index = int(input("请输入您想使用的功能编号(1-6):"))
            break
        except ValueError:
            print("警告：编号为数字形式!")
            continue
    
#循环
while True:
    input_num()
    result2 = menu()
    if result2 == "exit":
        break
    elif result2 == 1:
        print("继续使用！\n")
    else:
        print("无效选项！请重新输入正确的编号：")
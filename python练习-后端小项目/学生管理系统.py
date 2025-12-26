print("=========================")
print("学生管理系统 V10.0")
print("1,添加学生信息")
print("2,删除学生信息")
print("3,修改学生信息")
print("4,查询所有学生信息")
print("0,退出系统")
print("=========================")

info = []
index = 1

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
    elif input_index == 0:
        print("您已选择：退出系统")
        return "exit"
    return True

def index_1():
    global index,info
    print("以下是已有学生信息:")
    for i in info:
        print(i)
    print("您正在使用: 添加学生信息 功能")
    while True:
        try:
            name,sex,phone = input("请依次输入姓名，性别，手机号。中间用空格隔开。\n若要回到菜单,请在任意一格输入'e:\n").split()
            if name == 'e' or sex == 'e' or phone == 'e':
                break
            info.append({"序号":index,"姓名":name,"性别":sex,"手机号":phone})
            index += 1
            print("添加成功！")
            continue
        except ValueError:
            print("输入格式有误！请重新输入！")
            continue

def index_2():
    print("您正在使用: 删除学生信息 功能")
    # 展示学生方便选择序号。
    print("以下是已有学生信息:")
    for i in info:
        print(i)
    while True:
        name = input("请输入您想删除的学生的序号。\n若要回到菜单,输入'e':\n")
        if name == 'e':
            break
        for i in range(len(info)):
            if name == info[i]["序号"]:
                del info[i]
                print(f"已成功删除 {index}")
                continue
            else:
                print("查无此人！请重新输入。")
                continue

def index_3():
    print("您正在使用: 修改学生信息 功能")
    while True:
        if len(info) == 0:
            print("学生信息为空！退出修改程序")
            break
        # 展示学生方便选择序号。
        print("以下是已有学生信息:")
        for i in info:
            print(i)
        try:
            index = int(input("请输入要修改学生的序号:"))
            name,sex,phone = input("请依次输入修改后的学生姓名，性别，手机号。中间用空格隔开。\n若要回到菜单,请在任意一格输入'e:\n").split()
            if name == 'e' or sex == 'e' or phone == 'e':
                break
            # 字典没有replace方法..直接赋值
            info[index]["姓名"] = name
            info[index]["性别"] = sex
            info[index]["手机号"] = phone
            print(f"修改成功！您已将{index}号学生的信息修改为:{info[index]["姓名"]},{info[index]["性别"]},{info[index]["手机号"]}")
            continue
        except ValueError:
            print("输入格式有误！请重新输入！")
            continue

def index_4():
    print("您正在使用: 查询所有学生信息 功能")
    print("以下是所有学生信息:")
    for i in info:
        print(i)
# 输入部分
def input_num():
    # 定义全局变量
    global input_index
    while True:
        try:
            input_index = int(input("请输入您想使用的功能编号(1-0):"))
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
        print("继续使用本系统！\n")
    else:
        print("无效选项！请重新输入正确的编号：")
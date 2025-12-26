def menu():
    print(
    '''
    欢迎使用用户账户管理程序！
    1. 用户注册
    2. 用户登录
    3. 用户注销
    4. 修改密码
    5. 退出
    ''')


with open('file.txt','w') as file:
    pass

def sel():
    index = input("请输入您想使用的功能：") 
    if index == "1":
        while index_1():
            print("继续此功能！")
    elif index == "2":
        while index_2():
            print("继续此功能！")
    elif index == "3":
        while index_3():
            print("继续此功能！")
    elif index == "4":
        while index_4():
            print("继续此功能！")
    elif index == "5":
        return False
    else:
        print("请输入有效的选项！")
        return "remake"
    return True

def index_1():
    if exit1() == False:
        return False
    user_name = input("请输入您的用户名：")
    with open('file.txt','r') as file:
        content = file.read()
        if user_name in content:
            print("用户已注册！")
        else:
            user_password = input("请输入您的密码：")
            with open('file.txt','a') as file:
                file.write(f"{user_name}:{user_password}\n")
    return True

def index_2():
    if exit1() == False:
        return False
    user_name = input("请输入您的用户名：")
    user_password = input("请输入您的密码：")
    with open('file.txt','r') as file:
        if f"{user_name}:{user_password}" in file.read():
            print("登陆成功！")
        else:
            print("用户名或密码不正确！")
    return True

def index_3():
    if exit1() == False:
        return False
    user_name = input("请输入您的用户名：")
    user_password = input("请输入您的密码：")
    with open('file.txt','r') as file:
        content = file.read()
        if f"{user_name}:{user_password}" in content:
            target = f"{user_name}:{user_password}"
            # 前面已经读取过了，这里还原读取进度
            file.seek(0)
            lines = file.readlines()
        else:
            print("用户名或密码不正确！")
            return "remake"
    with open('file.txt','w') as file:   
        # 用覆盖文件，过滤相同的行 
        file.writelines(line for line in lines if line.strip() != target)
    print("注销成功！")
    return True

def index_4():
    if exit1() == False:
        return False
    user_name = input("请输入您的用户名：")
    user_password = input("请输入您的密码：")
    with open('file.txt','r') as file:
        content = file.read()
        if f"{user_name}:{user_password}" in content:
            target = f"{user_name}:{user_password}"
            # 操作同index3
            file.seek(0)
            lines = file.readlines()
            new_password = input("请输入新的密码！")
        else:
            print("用户名或密码不正确！")
            return "remake"            
    new_target = f"{user_name}:{new_password}\n"
    with open('file.txt','w') as file:
        for i in lines:
        # 用覆盖操作，和index_3相同思想
            if i.strip() == target:
                file.write(new_target)
            else:
                file.write(i)
    return True 

def exit1():
    exit = input("若想退出程序,请输入0,否则请随意输入:")
    if exit == '0':
        return False
    return True

def xunhuan():
    while True:
        menu()
        result = sel()
        if result == False:
            print("您已成功退出程序！")
            break
        elif result == "remake":
            pass
        else:
            print("继续使用！")

xunhuan()
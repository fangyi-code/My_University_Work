# 登录系统_账号密码检测
# 全局变量
print("登录系统")
stored_id = ""
stored_password = ""


# 设置账号密码
def id():
    # 函数内部只能读取全局变量，不能修改。修改要用global。
    global stored_id, stored_password
    user_id = input("请设置您的账号：")
    user_password = input("请设置您的密码：")
    # 如果没有global，函数内部会创建局部变量stored_id.
    if user_id != "" and user_password != "":
        # 这里赋值后，输入的数据被存储到全局。
        stored_id = user_id
        stored_password = user_password
        print("用户名密码设置成功")
    else:
        # 如果失败 重新调用函数
        print("用户名密码不得为空，请重新设置\n")
        id()


# 登录账户
def test():
    # 函数内部只能读取全局变量，不能修改。修改要用global。
    global stored_id, stored_password
    print("用户名密码区分大小写。")
    test_id = input("请输入您的账号：")
    test_password = input("请输入您的密码：")
    # 成功读取前面被修改后的全局变量
    if test_id == stored_id and test_password == stored_password:
        return True
    # 登录失败 返回后开始计数
    else:
        if nums>1:
            print("用户名或密码错误，请重新输入。")
        return False


# 方便用于模块导入。让代码既可以独立运行，也可被导入。不会自动执行登录流程。
if __name__ == "__main__":
    # 设置账号密码：
    id()
    # 登录成功后结束循环
    win = 0
    # 反复验证账号密码：
    while True:
        # 可选择
        if win == 1:
            break
        b = input("是否要登录账户?登录账户请输入'1':")
        if b != "1":
            break
        else:
            # 三次计数
            nums = 3
            while nums > 0:
                if test():
                    print("登录成功！")
                    win = 1
                    break
                else:
                    nums -= 1
                    if nums > 0:
                        # 动态计数
                        print(f"您还有 {nums} 次机会")
                    else:
                        print("输入错误次数过多，请稍后再试")
                        break
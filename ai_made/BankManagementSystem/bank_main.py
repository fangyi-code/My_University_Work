# bank_main.py
#    id = "admin"
#    password = "12345"

import json
import random


class Bank():
    def __init__(self):
        self.data_file = "bank_data.txt"
        self.dict = {}
        self.lock_dict = {}
        self.read_file()

    # 在 Bank 类中添加：
    def show_all_accounts(self):
        """显示所有账户信息（管理员专用）"""
        if not self.dict:
            print("暂无账户信息！")
            return
        
        print("\n" + "="*60)
        print("账户列表:")
        print("="*60)
        for card_id, info in self.dict.items():
            print(f"卡号: {card_id}")
            print(f"  姓名: {info['姓名']}")
            print(f"  身份证号: {info['身份证号']}")
            print(f"  手机号: {info['手机号']}")
            print(f"  余额: {info['金额']}元")
            if card_id in self.lock_dict:
                print(f"  状态: 🔒 已锁定")
            else:
                print(f"  状态: ✅ 正常")
            print("-"*40)
        
        print(f"总账户数: {len(self.dict)}")
        print(f"已锁定账户数: {len(self.lock_dict)}")
        print("="*60)

    def save_file(self):
        with open(self.data_file, "w") as f:
            json.dump({
                "账户信息": self.dict,
                "锁定账户信息": self.lock_dict
            }, f)

    def read_file(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.dict = data.get("账户信息", {})
                self.lock_dict = data.get("锁定账户信息", {})
        except (FileNotFoundError, json.JSONDecodeError):
            # 第一次运行或文件格式错误
            self.dict = {}
            self.lock_dict = {}

    def open_an_account(self):
        name = input("请输入姓名:")
        id_number = input("请输入身份证号:")
        phone_number = int(input("请输入手机号:"))
        money = int(input("请输入预存金额:"))
        password = input("请输入密码:")
        info = {
            "姓名": name,
            "身份证号": id_number,
            "手机号": phone_number,
            "金额": money,
            "密码": password
        }
        while True:
            card_id = str(random.randint(100000, 999999))
            if card_id not in self.dict:
                break

        self.dict[card_id] = info
        print(f"您的卡号为:{card_id},请妥善保存！")
        self.save_file()

    def check(self):
        card_id = input("请输入卡号:")
        if card_id not in self.dict:
            print("卡号不存在！")
            return
        if card_id in self.lock_dict:
            print("您的卡号已被锁定，无法进行此操作！")
            return
        n = 0
        while n < 3:
            password = input("请输入密码:")
            if password == self.dict[card_id]["密码"]:
                break
            else:
                print("密码错误！请重新输入。")
                n += 1
            if n == 3:
                print("卡号被锁定！")
                self.lock_dict[card_id] = self.dict[card_id]
                self.save_file()
                return

        print(f"您的余额为:{self.dict[card_id]['金额']}")

    def withdraw(self):
        card_id = input("请输入卡号:")
        if card_id not in self.dict:
            print("卡号不存在！")
            return
        if card_id in self.lock_dict:
            print("您的卡号已被锁定，无法进行此操作！")
            return
        n = 0
        while n < 3:
            password = input("请输入密码:")
            if password == self.dict[card_id]["密码"]:
                break
            else:
                n += 1
            if n == 3:
                print("卡号被锁定！")
                self.lock_dict[card_id] = self.dict[card_id]
                self.save_file()
                return

        print(f"您的余额为:{self.dict[card_id]['金额']}")
        withdraw_money = int(input("请输入取款金额:"))
        if self.dict[card_id]["金额"] < withdraw_money or withdraw_money < 0:
            print("余额不足或输入了无效数字:取款无效！")
            return
        self.dict[card_id]["金额"] = self.dict[card_id]["金额"] - withdraw_money
        self.save_file()
        print(f"您的余额为:{self.dict[card_id]['金额']}")

    def deposit(self):
        card_id = input("请输入卡号:")
        if card_id not in self.dict:
            print("卡号不存在！")
            return
        if card_id in self.lock_dict:
            print("您的卡号已被锁定，无法进行此操作！")
            return
        n = 0
        while n < 3:
            password = input("请输入密码:")
            if password == self.dict[card_id]["密码"]:
                break
            else:
                n += 1
            if n == 3:
                print("卡号被锁定！")
                self.lock_dict[card_id] = self.dict[card_id]
                self.save_file()
                return

        print(f"您的余额为:{self.dict[card_id]['金额']}")
        deposit_money = int(input("请输存款金额:"))
        if deposit_money < 0:
            print("存款金额无效！")
            return
        self.dict[card_id]["金额"] = self.dict[card_id]["金额"] + deposit_money
        self.save_file()
        print(f"您的余额为:{self.dict[card_id]['金额']}")

    def transfer(self):
        card_id = input("请输入卡号:")
        if card_id not in self.dict:
            print("卡号不存在！")
            return
        if card_id in self.lock_dict:
            print("您的卡号已被锁定，无法进行此操作！")
            return
        n = 0
        while n < 3:
            password = input("请输入密码:")
            if password == self.dict[card_id]["密码"]:
                break
            else:
                n += 1
            if n == 3:
                print("卡号被锁定！")
                self.lock_dict[card_id] = self.dict[card_id]
                self.save_file()
                return

        in_card_id = input("请输入转入卡号:")
        if in_card_id not in self.dict:
            print("未查询到此卡号！")
            return
        while True:
            trans_money = int(input("请输入转账金额！"))
            while True:
                tf = input("是否进行转账？若要取消,请输入'n':\n")
                if tf == 'n':
                    print("您已取消转账！回退到上一个页面！")
                    break
                while True:
                    try:
                        if trans_money > self.dict[card_id]["金额"]:
                            print("余额不足，请重新输入。")
                            continue
                        break
                    except ValueError:
                        print("请输入阿拉伯数字！")
                        continue
                self.dict[card_id]["金额"] = self.dict[card_id]["金额"] - trans_money
                self.dict[in_card_id]["金额"] = self.dict[in_card_id]["金额"] + trans_money
                self.save_file()
                print(f"您已完成转账！您的余额为:{self.dict[card_id]['金额']}")
                break
            break

    def lock(self):
        card_id = input("请输入卡号:")
        if card_id not in self.dict:
            print("卡号不存在！")
            return
        if card_id in self.lock_dict:
            print("您的卡号已被锁定，无法进行此操作！")
            return
        password = input("请输入密码:")
        if password == self.dict[card_id]["密码"]:
            print("卡号被锁定！")
            self.lock_dict[card_id] = self.dict[card_id]
            self.save_file()
            return
        print("账号密码错误！返回菜单。")

    def unlock(self):
        card_id = input("请输入卡号:")
        if card_id not in self.dict:
            print("卡号不存在！")
            return
        password = input("请输入密码:")
        if password == self.dict[card_id]["密码"]:
            print("卡号已解锁！")
            del self.lock_dict[card_id]
            self.save_file()
            return
        print("账号密码错误！返回菜单。")

    def exit(self):
        id = "admin"
        password = "12345"

        input_id = input("请输入管理员账户：")
        if input_id != id:
            print("管理员账户输入错误")
            return
        input_password = input("请输入密码：")
        if input_password != password:
            print("输入密码有误")
            return
        if input_id == id and input_password == password:
            print("操作成功，请稍后")
            # return -1 代表退出系统
            return -1


def welcome():
    print('*' * 42)
    for i in range(5):
        if i != 2:
            print('*' * 3, '*' * 3, sep=' ' * 36)
        else:
            print('*' * 3, '欢迎登陆银行管理系统', '*' * 3, sep=' ' * 10)
    print('*' * 42)


def login():
    id = "admin"
    password = "12345"

    input_id = input("请输入管理员账户：")
    if input_id != id:
        print("管理员账户输入错误")
        return -1
    input_password = input("请输入密码：")
    if input_password != password:
        print("输入密码有误")
        return -1
    if input_id == id and input_password == password:
        print("操作成功，请稍后")
        menu()


def menu():
    bank = Bank()
    while True:
        print('*' * 42)
        print('*** 1. 开户(1)         2. 查询(2)    ***')
        print('*** 3. 取款(3)         4. 存款(4)    ***')
        print('*** 5. 转账(5)         6. 锁定(6)    ***')
        print('*** 7. 解锁(7)                      ***')
        print('*** 退出(Q)                         ***')
        print('*' * 42)
        index = input("请输入您想使用的功能(1-Q):")
        if index == '1':
            bank.open_an_account()
        elif index == '2':
            bank.check()
        elif index == '3':
            bank.withdraw()
        elif index == '4':
            bank.deposit()
        elif index == '5':
            bank.transfer()
        elif index == '6':
            bank.lock()
        elif index == '7':
            bank.unlock()
        elif index == 'Q':
            result = bank.exit()
            if result == -1:
                print("系统已退出！")
                break
        else:
            print("请输入有效的数字！")


# 在 bank_main.py 中添加角色选择函数

def admin_menu():
    """管理员专用菜单"""
    bank = Bank()
    while True:
        print('*' * 50)
        print('***        银行管理系统 - 管理员功能        ***')
        print('*' * 50)
        print('*** 1. 开户(1)         2. 锁定账户(2)    ***')
        print('*** 3. 解锁账户(3)     4. 显示所有账户(4) ***')
        print('*** 退出(Q)                             ***')
        print('*' * 50)
        
        index = input("请选择功能(1-4, Q退出):")
        
        if index == '1':
            bank.open_an_account()
        elif index == '2':
            bank.lock()
        elif index == '3':
            bank.unlock()
        elif index == '4':
            # 显示所有账户（需要添加这个功能）
            bank.show_all_accounts()
        elif index.upper() == 'Q':
            result = bank.exit()
            if result == -1:
                print("系统已退出！")
                break
        else:
            print("请输入有效的数字！")

def customer_menu():
    """客户专用菜单"""
    bank = Bank()
    while True:
        print('*' * 50)
        print('***        银行管理系统 - 客户功能         ***')
        print('*' * 50)
        print('*** 1. 查询(1)         2. 取款(2)       ***')
        print('*** 3. 存款(3)         4. 转账(4)       ***')
        print('*** 退出(Q)                             ***')
        print('*' * 50)
        
        index = input("请选择功能(1-4, Q退出):")
        
        if index == '1':
            bank.check()
        elif index == '2':
            bank.withdraw()
        elif index == '3':
            bank.deposit()
        elif index == '4':
            bank.transfer()
        elif index.upper() == 'Q':
            print("退出客户系统！")
            break
        else:
            print("请输入有效的数字！")

def main():
    welcome()
    print("\n请选择角色:")
    print("1. 管理员")
    print("2. 客户")
    print("3. 退出")
    
    choice = input("请选择 (1-3): ")
    
    if choice == '1':
        admin_menu()
    elif choice == '2':
        customer_menu()
    elif choice == '3':
        print("系统已退出！")
    else:
        print("无效选择！")

if __name__ == "__main__":
    main()
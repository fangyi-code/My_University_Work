# 在这种几个输入需要满足不同条件的情况下，需要嵌套if或者连续几个if分支，而不是if-elif
from string import digits

print("----------------------")
menu = {
    '可口可乐':'2.5元',
    '百事可乐':'2.5元',
    '冰红茶':'3元',
    '脉动':'3.5元',
    '果缤纷':'3元',
    '绿茶':'3元',
    '茉莉花茶':'3元',
    '尖叫':'2.5元'
}
for key,value in menu.items():
    print(f"{key} : {menu[key]}")
print("----------------------")
sum = 0

# 输入部分
def input_word():
    print("请输入需要的饮品名称和数量,若已完成选择,输入'q'进行结算。")
    while True:
        try:
            name,num = input().split()
            if name == 'q':
                money()
                # 跳出循环
                break
            if name not in menu:
                print("饮品名称不正确！")
                # 跳过之后所有，立刻开始下一次循环
                continue
                # 数量检查,引入string中的isdigit（）方法
            if int(num)<0 or not num.isdigit():
                print("饮品数量不合法！")
                continue
            # 三轮判断后调用cal（）函数，传参，调用完成后依然在while中，直到结算。
            cal(name,num)

        except ValueError:
            print("输入格式错误，请按照“名称” “数量”输入，中间为空格")
            continue
# 计算部分
def cal(name,num):
    global sum
    price = menu[name]
    price = float(price.replace("元",""))
    sum += price * int(num)

# 结算部分
def money():
    print(sum)
    return True

# 循环部分
while True:
    input_word()
    if money():
        break
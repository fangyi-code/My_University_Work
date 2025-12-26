print("欢迎来到文字排版工具！在该工具中可以输入要排版的文字。")
print("该工具共有5个功能:")
print("删除空格(编号1)")
print("英文标点替换(编号2)")
print("段落分割(编号3)")
print("字母大写(编号4)")
print("退出(编号0)")
# 菜单
def menu():
    # 全局变量
    global input_word
    # 判断部分
    if input_index == "1":
        print(input_word.replace(" ",""))
    elif input_index == "2":
        # 多次替换，利用字典和for遍历
        replace_dict = {
            ",": "，",
            ".": "。", 
            "?": "？",
            "!": "！",
            ":": "："
        }
        for old,new in replace_dict.items():
            input_word = input_word.replace(old,new)
        print(input_word)
    elif input_index == "3":
        print(input_word.replace("\r\n","\n\n"))
    elif input_index == "4":
        # 利用大写函数
        print(input_word.upper())
    elif input_index == "0":
        print("感谢您的使用！")
        # return直接返回循环部分
        return "exit"
    # 输入错误编号
    else:
        return False
    return True

# 循环
while True:
    # 修改前的文字和修改后的文字
    input_index = input("请输入您想使用的功能编号:")
    input_word = input("请输入您想要排版的文字:")    # 善用return！！
    result = menu()
    if result == "exit":
        break
    elif result == 1:
        print("继续使用文字排版工具！\n")
    else:
        print("无效选项！请重新输入正确的编号：")
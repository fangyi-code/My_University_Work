#叁 肆 伍 陆 柒 捌 玖
print("欢迎使用中文数字对照表！")
word = 0

# 转换部分
def trans():
    dict = {
    0:"零", 1:"壹", 2:"贰", 3:"叁", 4:"肆",
    5:"伍", 6:"陆", 7:"柒", 8:"捌", 9:"玖",
}
    # get：字典的方法，可以根据键取值。返回的是值或者None。
    return dict.get(word)

# 输入部分
def input_words():
    global word
    # 防止输入出现问题
    while True:
        try:
            word = int(input("请输入您想转换的阿拉伯数字(0-9):"))
            break
        except ValueError:
            print("警告！请输入一个数字")
            continue    

# 循环部分
while True:
    input_words()
    result = trans()
    if result is not None:
        print(result)
        print("已成功输出，感谢您的使用！")
    else:
        print("输入有误,本程序仅可以识别0-9之间的数字")
        
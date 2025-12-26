print("这是一个智能聊天机器人，有三项功能：训练，对话和离开。")
print("训练机器人请输入't'")
print("与机器人对话请输入'c'")
print("要离开，请输入'1',您将退出程序。")
dict = {'诗仙是谁':'李白',
'中国第一个朝代是哪个朝代':'夏朝',
'三十六计的第一计是什么':'瞒天过海',
'“天府之国”是中国的哪个地方':'四川',
'中国第一长河是哪条河':'长江'}

# 输入
def input_word():
    input_word = input("请输入您想使用的功能:")
    if input_word == 't':
        practice()
    elif input_word == 'c':
        talk()
    elif input_word == '1':
        return 'exit'
    else:
        print("请输入有效的字符！")

        
# 训练
def practice():
    global dict
    print("已进入训练窗口：")
    question = input("请输入您想训练的问题:")
    answer = input("请输入问题的答案:")
    dict[question] = answer
    print(f"机器人已成功学会：{dict}")

# 对话
def talk():
    # 普通写法
    # while True:
        print("已进入对话窗口：")
        # key方法
        for key in dict.keys():
            print(f"目前机器人已学会的问题有:{key}")
        question = input("请输入您的问题！仅限机器人已学会的问题哦~要退出请输入“exit”")
        # if question in dict:
        #     print(f"{question} 的答案是: dict[question]")
        # elif question == "exit":
        #     break
        # else:
        #     print("机器人尚未学会此问题！请重新输入～您将重新进入对话窗口。")
    # 递归
        if question == 'exit':
            # 退出
            return True 
        if question in dict:
            print(f"{question} 的答案是: {dict[question]}!")
        else:
            print("机器人尚未学会此问题！请重新输入～")
        # 用递归来实现无限循环（python限制1000层以内）
        talk()

            

# 循环
while True:
    if input_word() != 'exit':
        continue
    else:
        print("您已成功退出程序！")
        break
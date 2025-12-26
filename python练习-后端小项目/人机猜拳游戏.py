# 需要有玩家基类，下分机器和人类。人类通过输入来选择手势。
# 需要有手势类
# 需要有判定规则类
import random

class Player:
    def __init__(self,name):
        self.name = name 
        self.score = 0
        self.history = []

class ai_player(Player):
    def choose(self,human_history):
        if len(human_history) == 0:
            # randint:随机生成（a，b）范围内的整数
            choice = random.randint(1,3)
        else:
            count = {1:0,2:0,3:0}
            for h in human_history:
                count[h]+=1
            # count.get:获取值
            # key = count.get:用值来比较，而不是键,最终返回值最大的键
            max_count = max(count,key = count.get)
            # 1: "石头", 2: "剪刀", 3: "布"
            win = {1:3,2:1,3:2}
            # 此时人类手势是键
            choice = win[max_count]
        self.history.append(choice)
        #返回选择的手势
        return choice

class human_player(Player):
    def choose(self):
        while True:
            try:
                choice = int(input(f"{self.name}请选择:1.石头 2.剪刀 3.布: "))
                if choice in [1,2,3]:
                    self.history.append(choice)
                    # 返回选择的手势
                    return choice
                else:
                    print('"请输入1-3之间的数字"')
            except ValueError:
                print("请输入有效数字")

class Rules:
    gestures = {1: "石头", 2: "剪刀", 3: "布"}
    def judge(self,choice1,choice2):
        # 平局
        if choice1 == choice2:
            return 0
        # 获胜情况
        win = [(1,2),(2,3),(3,1)]
        if (choice1,choice2) in win:
            return 1
        return 2

def main():
    print("欢迎来到人机猜拳游戏！")
    human = human_player("玩家")
    ai = ai_player("计算机")
    rules = Rules()
    while True:
        print(f"当前比分:{human.score}:{ai.score}")
        human_choice = human.choose()
        ai_choice = ai.choose(human.history)
        print(f"您出了:{rules.gestures[human_choice]}")
        print(f"计算机出了:{rules.gestures[ai_choice]}")
        result = rules.judge(human_choice,ai_choice)
        if result == 0:
            print("平局！")
        elif result == 1:
            print("你赢了！")
            # 子类可以继承父类的属性
            human.score += 1
        else:
            print("电脑赢了！")
            ai.score += 1
        
        n = input("继续？(1/0): ")
        if n != '1':
            break
    
    print(f"最终比分: {human.score} : {ai.score}")

main()
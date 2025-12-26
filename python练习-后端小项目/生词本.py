from ast import NodeTransformer
import random

print("="*25)
print("1. 查看单词")
print("2. 背单词") 
print("3. 添加新单词")
print("4. 删除单词")
print("5. 清空生词本")
print("6. 退出")
print("="*25)

class Books():
    def __init__(self):
        self.words = {}

    def save(self):
        # w写入并覆盖
        # 注：word.txt在当前目录下
        with open("words.txt", "w") as f:
            # 覆盖全部
            for word, trans in self.words.items():
                f.write(f"{word}|{trans}\n")
        print("单词已自动保存到文件！")


    def view(self):
        if len(self.words) == 0:
            print("生词本为空！")
        else:
            for key,value in self.words.items():
                print(f'{key}:{value}')
        return True

    def recite(self):
        if len(self.words) == 0:
            print("生词本为空！")
            return True
        # random.choice可以随机选取
        random_key = random.choice(list(self.words))
        print(random_key)
        print("这个单词的意思是:")
        while True:
            ans = input()
            if ans == self.words[random_key]:
                print("太棒了！")
                return True
            else:
                print("再想想")
        

    def add(self):
        word = input("请输入您想要添加的单词：")
        trans = input("请输入单词的翻译：")
        if word in self.words:
            print("单词已存在！")
        else:
            self.words[word] = trans
            self.save()
            print("已成功添加！")

    def delete(self):
        if len(self.words) == 0:
            print("生词本为空！")
        word = input("请输入您想要删除的单词：")
        if word in self.words:
            print("单词已删除！")
            del self.words[word]
            self.save()
        else:
            print("单词不存在")


    def delete_all(self):
        self.words.clear()
        self.save()
        print("清空成功！")

def menu(input_index):     
    #判断部分
    if input_index == 1:
        books.view()
    elif input_index == 2:
        books.recite()
    elif input_index == 3:
        books.add()
    elif input_index == 4:
        books.delete()
    elif input_index == 5:
        books.delete_all()
    elif input_index == 6:
        return "exit"
    else:
        print("错误！")
    return True

# 保证只调用一个实例！
books = Books()

while True:
    try:
        input_index = int(input("请选择功能(1-6): "))
        result = menu(input_index)
        if result == "exit":
            print("退出生词本！")
            break
    except ValueError:
        print("请输入数字！")
        continue


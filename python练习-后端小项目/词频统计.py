# 有没有搞错？？咋这么难？？？难死了！！！
print("欢迎来到词频统计器！")

def cal():
    list = []
    for i in input_str:
        # 去除标点符号(在遍历字符串时，空格也会被取到)
        if ('a'<= i <='z') or i == ' ':
            list.append(i)
        else:
            list.append(" ")
        # join是字符串对象的方法！可迭代的元素必须都是字符串
        new_str = ''.join(list) # 此时输入的文本去除了标点符号，并且都是小写
        new_list = [x for x in new_str.split() if x]
    return new_list


while True:
    input_str = input("请输入一段英文文本:").lower()

    words = cal()
    counts = {}
    for x in words:
        # counts[w]，看起来是counts[键],其实是键的对应值的位置
        # get(x,0)+1 代表没遇到就返回0，遇到一次就+1，总之get返回对应x的值
        counts[x] = counts.get(x,0)+1
#时间计算器
print("此时间计算器使用24小时制")

def calculation():
    hour1 = int(input("请输入起始时间的小时数："))
    minute1 = int(input("请输入起始时间的分钟数："))
    hour2 = int(input("请输入结束时间的小时数："))
    minute2 = int(input("请输入结束时间的分钟数："))
    print("\n")

    sum1 = abs(hour1-hour2)
    sum2 = abs(minute1-minute2)
    print(f"时间间隔为：{sum1}小时{sum2}分钟")

while True:
    calculation()
    #询问是否继续
    print("是否要继续操作？继续请输入“1”，输入其他字符均视为停止操作\n")
    a = input()
    if a != "1":
        break
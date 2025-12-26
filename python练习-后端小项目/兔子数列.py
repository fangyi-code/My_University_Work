# 第一个月1对，第二个月1对，第三个月2对，第四个月3对，第五个月5对，第六个月8对..
# n=1,f(n)=1
# n=2,f(n)=1
# n>=3时，f(n) = f(n-1) + f(n-2)
# 这绝对是我写过最艰难的一个单元的代码...首先递归不能加载while里 不然根本无法控制！
# 递归函数进行计算
def rabbit(month):
    if month == 1 or month == 2:
        return 1
    else:
        return rabbit(month-1) + rabbit(month-2)

# 输入部分
while True:
    try:
        month = int(input("请输入月份："))
        if month <= 0:
            print("请输入有效的月份！")
            continue
        result = rabbit(month)
        print("兔子的数量为:")
        print(result)
        continue
    except ValueError:
        print("请使用阿拉伯数字输入正确的月份！")

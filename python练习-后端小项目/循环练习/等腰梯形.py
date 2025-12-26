# 上底为8 下底为18
m = int(input("请输入上边长度"))
n = int(input("请输入下底长度"))
n += 2
for i in range(m,n,2):
    space = " "*((n-i)//2)
    stars = "*"*i
    print(space+stars)

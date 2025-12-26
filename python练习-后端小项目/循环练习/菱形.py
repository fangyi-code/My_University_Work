n = int(input("请输入菱形上半部分行数："))
for i in range(1,n+1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars)

for i in range(n-1,0,-1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars)
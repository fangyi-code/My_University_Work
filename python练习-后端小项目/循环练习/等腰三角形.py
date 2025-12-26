# 等腰三角形
n = 5
for i in range(1,n+1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars+spaces,end = "\n")
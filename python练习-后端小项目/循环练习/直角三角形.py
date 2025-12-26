# 打印一个直角三角形
# for i in range(1,10):
#     for i in range(1,i+1):
#         print("*",end = "")
#     print("")

for i in range(10,0,-1):
    for j in range(i-1):
        print(" ",end = "")
    print("*"*(11-i))
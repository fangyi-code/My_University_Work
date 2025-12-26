# 打印一个10*10的空心方形
for i in range(10):
    for j in range(10):
        if i==0 or i==9 or j==0 or j==9:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print(" ")
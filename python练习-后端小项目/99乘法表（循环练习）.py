# 此程序用于输出九九乘法表
# 循环嵌套
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}", end=" ")
    print("\n")
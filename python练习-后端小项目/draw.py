# 绘制五子棋棋盘
size = 0
print("此程序用来绘制五子棋棋盘")

def draw():
    # 修改全局变量
    global size
    # 控制棋盘尺寸
    size = int(input("请输入棋盘尺寸："))
    # 控制行数
    for i in range(size):
        # 列
        for j in range(size):
            # end=“”可取消换行
            print("+",end = "")
            # 不到末尾就输出
            if j<(size-1):
                print(" —— ",end="")
        # 输出一整行后进行换行
        print()
        # 控制竖线
        if i < (size-1):
            for j in range(size):
                print('|',end="")
                if j < size-1:
                    # 对齐
                    print("    ",end="")
            print()


# 循环程序
while True:
    # 调用函数
    draw()
    # 说明
    print(f"已生成{size}x{size}尺寸棋盘")
    # 决定是否循环
    print("是否需要开始新一轮绘制?如果是,请输入“1”:")
    a = input()
    # 否 比 是 更方便
    if a != "1":
        break

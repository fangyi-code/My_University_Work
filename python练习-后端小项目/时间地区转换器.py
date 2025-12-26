# 中国：YYYY年MM月 DD日 HH:mm:ss。
# 美国: MM/DD/YYYY HH:mm:ss。
# 英国、澳大利亚、法国：DD/MM/YYYY HH:mm:ss。
# 德国、俄罗斯：DD.MM.YYYY HH:mm:ss。
# 加拿大：YYYY-MM-DD HH:mm:ss。
print("这是一个时间地区转换器")


def trans():
    if area == "中国":
        print(f"{year}年{month}月{day}日 {hour}:{minute}:{second}。")
    elif area == "美国":
        print("{}/{}/{} {}:{}:{}。".format(month, day, year, hour, minute, second))
    elif area == "英国" or area == "澳大利亚" or area == "法国":
        print("%d/%d/%d %d:%d:%d。" % (day, month, year, hour, minute, second))
    elif area == "德国" or area == "俄罗斯":
        print(f"{day}.{month}.{year} {hour}:{minute}:{second}。")
    elif area == "加拿大":
        print(f"{year}-{month}-{day} {hour}:{minute}:{second}。")
    else:
        print("请您从:中国,美国,英国,澳大利亚,法国,德国,俄罗斯,加拿大这几个国家中选择一个进行转换,或输入exit退出")
        return False
    # 成功则跳出while循环 不成功返回循环
    return True


while True:
    # 主循环
    a = input("是否要使用时间地区转换器?\n若要使用,请输入任意字符;若不,请输入“exit“退出。")
    if a == "exit":
        print("您已选择:退出程序！")
        break
    # 输入部分
    year, month, day, hour, minute, second = map(int, input("请输入年,月,日,时,分,秒,输入时用空格隔开\n").split())
    # 循环进行判断
    while True:
        area = input("请输入您想转换的地区:\n")
        if trans():
            break

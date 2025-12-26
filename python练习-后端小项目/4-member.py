# 会员等级评定
# 根据消费金额评定：
def member_m():
    # 消费金额
    m= float(input("请输入消费金额："))
    if m >= 1000:
        return "您是钻石会员！"
    elif 500 <= m < 1000:
        return "您是白金会员！"
    elif 200 <= m < 500:
        return "您是黄金会员！"
    elif 100 <= m < 200:
        return "您是白银会员！"
    elif 50 <= m < 100:
        return "您是青铜会员！"
    else:
        return "您是普通会员！"


# 根据积分评定：
def member_s():
    # 消费金额
    s= float(input("请输入消费积分："))
    if s >= 10000:
        return "您是钻石会员！"
    elif 5000 <= s < 10000:
        return "您是白金会员！"
    elif 2000 <= s < 5000:
        return "您是黄金会员！"
    elif 1000 <= s < 2000:
        return "您是白银会员！"
    elif 500 <= s < 1000:
        return "您是青铜会员！"
    else:
        return "您是普通会员！"


# 循环判断：
while True:
    print("请选择会员等级评定方式，消费金额输入：1，积分输入：2")
    a = input("在此行输入：")
    if a == "1":
        result = member_m()
        print(result)
    if a == "2":
        result = member_s()
        print(result)

# 输出购物小票
from datetime import datetime
current_time = datetime.now().replace(microsecond=0)
# 物品
a = "金士顿U盘8G"
b = "胜创16GTF卡"
c = "读卡器"
d = "网线2米"
#数量
num = 0
#总金额
sum = 0.00
# 填写价格
aprice,bprice,cprice,dprice = map(float,input("""请输入商品价格，顺序为：
'金士顿U盘8G'
'胜创16GTF卡'
'读卡器'
'网线2米'\n""").split())
anum,bnum,cnum,dnum = map(int,input("""您已输入商品价格，请输入商品数量，顺序为：
'金士顿U盘8G'
'胜创16GTF卡'
'读卡器'
'网线2米'\n""").split())

# 支付流程
sum = anum*aprice+bnum*bprice+cnum*cprice+dnum*dprice
while True:
    pay = float(input(f"请付钱，总金额为{sum:.2f}元\n"))
    if pay >= sum:
        break
    else:
        sum -= pay
        print(f"金额不够，请再付{sum:.2f}元")

if aprice is not None and bprice is not None and cprice is not None and dprice is not None:
    print("···················································")
    print("单号：DH202311010001")
    print(f"时间：{current_time}")
    print("···················································")
    print("名称","数量","单价","金额",sep = '         ')
    print("%-10s %2d %10.2f %10.2f"%("金士顿U盘8G",anum,aprice,anum*aprice))
    print("%-10s %2d %10.2f %10.2f"%("胜创16GTF卡",bnum,bprice,bnum*bprice))
    print("%-10s %2d %10.2f %10.2f"%("读卡器",cnum,cprice,cnum*cprice))
    print("%-10s %2d %10.2f %10.2f"%("网线2米",dnum,dprice,dnum*dprice))
    print("···················································")
    print("总数:",anum+bnum+cnum+dnum,"         总额：",sum)
    print("折后总额：",sum)
    print("实收：",pay,"      找零：",pay-sum)
    print("收银：管理员")
    print("···················································")
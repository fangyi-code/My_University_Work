# 这是一个房贷计算器
# 1为商业贷款，2为公积金贷款
# 商业贷款利率为4.75%和4.9%。公积金贷款利率为2.6%和3.1%
business_short = 0.049
business_long = 0.0475
provident_short = 0.031
provident_long = 0.026

def cal_formula(type):
    # 每月月供参考：
    loan_month = loan_amount * ((type / 12) * (1 + type / 12) ** (loan_year * 12)) / (
                ((1 + type / 12) ** (loan_year * 12)) - 1)
    # 还款总额：
    loan_sum = loan_month * loan_year * 12
    # 总利息：
    interest = loan_sum - loan_amount
    return loan_month, loan_sum, interest

def loan_1():
    if loan_year <= 5:
        loan_month, loan_sum, interest = cal_formula(business_short)
    else:
        loan_month, loan_sum, interest = cal_formula(business_long)
    print(f"您的每月月供参考为：{loan_month:.2f}\n您的还款总额为：{loan_sum:.2f}\n您的总利息为：{interest:.2f}\n")

def loan_2():

    if loan_year <= 5:
        loan_month, loan_sum, interest = cal_formula(provident_short)
    else:
        loan_month, loan_sum, interest = cal_formula(provident_long)
    print(f"您的每月月供参考为：{loan_month:.2f}\n您的还款总额为：{loan_sum:.2f}\n您的总利息为：{interest:.2f}\n")




print("这是一个房贷计算器")

while True:
    loan_type = input("请输入贷款类型:1,商业贷款。2,公积金贷款。(输入序号或名称均可),按exit键可退出计算器\n")
    if loan_type == "exit":
        print("您已退出房贷计算器！")
        break

    loan_amount = float(input("请输入您的贷款金额："))
    loan_year = int(input("请输入您的贷款年限："))

    if loan_type == "1" or loan_type == "商业贷款":
        loan_1()
    elif loan_type == "2" or loan_type == "公积金贷款":
        loan_2()
    else:
        print("请输入有效的数字或文字,或按exit键退出计算器。")
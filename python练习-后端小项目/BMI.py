print("这是一个BMI计算器")
#利用float强制转换str为浮点型
weight = float(input("请输入您的体重，单位为kg："))
height = float(input("请输入您的身高，单位为m："))
bmi = weight/(height**2)
#格式化字符串
print(f"您的BMI指数为：{bmi:.2f}")
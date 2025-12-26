class Calculator(object):
    def __init__(self, number, L):
        self.number = number 
        self.L = L

    def add(self):
        new_L = []
        # 只调用一个实例，所以要使用临时变量，防止number的值被修改
        temp = self.number
        for other in self.L:
            temp = temp + other 
            new_L.append(temp)
        return new_L

    def sub(self):
        new_L = []
        temp = self.number
        for other in self.L:
            temp = temp - other 
            new_L.append(temp)
        return new_L

    def mul(self):
        new_L = []
        temp = self.number
        for other in self.L:
            temp = temp * other 
            new_L.append(temp)
        return new_L

    def truediv(self):
        new_L = []
        temp = self.number
        for other in self.L:
            temp = temp / other 
            new_L.append(temp)
        return new_L

calculator = Calculator(10, [1,2,3])
print(calculator.add()) 
print(calculator.sub()) 
print(calculator.mul()) 
print(calculator.truediv())
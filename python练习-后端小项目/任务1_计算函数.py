class calculate:
    def __init__(self,operator,*args,**kwargs):
        self.operator = operator
        self.args = args
        self.kwargs = kwargs

    def judge(self):
        if self.operator == 'add':
            result = self.add()
        elif self.operator == 'subtract':
            result = self.subtract()
        elif self.operator == 'multiply':
            result = self.multiply()
        elif self.operator == 'divide':
            result = self.divide()
        else:
            raise ValueError(f"不支持的操作符: {self.operator}")

        precision = self.kwargs.get('precision')
        result = round(result,precision) if precision is not None else result
        return result
    def add(self):
        return sum(self.args)

    def subtract(self):
        a = self.args[0]
        num = 0
        n = len(self.args)
        for i in range(1,n):
            num += a - self.args[i]
        return num

    def multiply(self):
        a = self.args[0]
        n = len(self.args)
        for i in range(1,n):
            a *= self.args[i]
        return a

    def divide(self):
        a = self.args[0]
        n = len(self.args)
        for i in range(1,n):
            if self.args[i] == 0:
                print("此处除数为0！")
            else:
                a /= self.args[i]
        return a

if __name__ == "__main__":
    print("="*50)
    print("任务1 测试")
    print("="*50)
    # 测试calculate 函数
    # 示例调用:
    print(calculate('add', 1.1111, 2.2222, 3.3333, precision=2).judge()) # 应输出6.67
    print(calculate('subtract',100,30,50).judge()) # 应输出20
    print(calculate('multiply', 2, 3, 4).judge()) # 应输出24
    print(calculate('divide', 10, 3, 3, precision=3).judge()) # 应输出1.111
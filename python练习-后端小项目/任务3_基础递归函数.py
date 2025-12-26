def factorial(n):
    if n == 0:
        return 1
    sum = n*factorial(n-1)
    return sum

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    return result


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = base * power(base, exponent-1)
    elif exponent < 0:
        result = base * power(base, -exponent)
    return result


if __name__ == "__main__":
    print("="*50)
    print("任务1 测试：基础递归函数")
    print("="*50)
    print("阶乘(5):", factorial(5)) # 120
    print("斐波那契(10):", fibonacci(10)) # 55
    print("幂运算(2^8):", power(2, 8)) # 256
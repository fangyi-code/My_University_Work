global_var = 10

def outer():
    local_var = 20
    global global_var
    global_var = global_var + 100
    def inner():
        nonlocal local_var
        global global_var
        local_var *=2
        global_var = global_var + 50
        return f"Inner:local_var = {local_var}, global_var = {global_var}"
    result = inner()
    print(result)

if __name__ == "__main__":
    print("\n" + "="*50)
    print("任务2 测试")
    print("="*50)
    # 测试全局变量和嵌套函数
    outer()
    print(f'全局最终:global_var={global_var}')
    # 预期输出:
    # Inner: local_var = 40, global_var = 160
    # 全局最终: global_var = 160
from tabnanny import check


class Invalid_input(Exception):
    def __str__(self):
        return "Invalid input:无效输入，请输入有效的数字或中文！"


class Anti_Scam:
    def __init__(self,path = "info.txt"):
        self.dict = path
        self.content = None

    def save_file(self,content,mode):
        # 想完成改变部分的操作，要读取-修改-写入
        data = {}
        try:
            with open(self.dict,'r') as f:
                for i in f:
                    # 去掉前后空格，按照冒号分割1次
                    key,value = i.strip().split(":",1)
                    data[key] = int(value)
        except FileNotFoundError:
            pass
        
        if mode == 'check':
            if content in data:
                return data[content]
            else:
                print("查询不到该手机号/网址。")
                return 
        
        elif mode == 'report':
            if content in data:
                data[content] += 1
            else:
                data[content] = 1
            
            with open(self.dict,'w') as f:
                for key,value in data.items():
                    f.write(f"{key}:{value} \n")
                print(f"{data[key]}")
            return data[content]

    def user_input(self):
        while True:
            try:
                choice = input("请输入您要举报/查询的内容:1,手机号。2,网址:")
                if choice == "1" or choice == "手机号":
                    phone = input("请输入您要举报/查询的手机号:")
                    return phone
                elif choice == "2" or choice == "网址":
                    web = input("请输入您要举报/查询的网址:")
                    return web
                else:
                    raise Invalid_input()
                    
            except Invalid_input as error:
                print(error) 
                continue

    def check(self):
        c = self.save_file(content = self.user_input(),mode = 'check')
        if c:
            print(f"该手机号/网址被标记{c}次")

    def report(self):
        r = self.save_file(content = self.user_input(),mode = 'report')
        if r:
            print(f"举报成功！该手机号/网址被标记{r}次")

def main():
    anti_scam = Anti_Scam()
    while True:
        op = input("\n请选择功能:1.查询 2.举报 3.退出: ")
        if op == "1":
            anti_scam.check()
        elif op == "2":
            anti_scam.report()
        elif op == "3":
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入")

main()
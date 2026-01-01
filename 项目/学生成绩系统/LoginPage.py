import tkinter as tk 
from tkinter import messagebox
from db import db
from MainPage import MianPage

class LoginPage:
    def __init__(self,master):
        # 主窗口
        self.root = master
        self.root.geometry('500x300')
        self.root.title('登录页')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # 框架
        self.page = tk.Frame(root)
        self.page.pack()

        # grid-网格
        tk.Label(self.page).grid(row = 0,column = 0)

        tk.Label(self.page, text = '账户: ').grid(row = 1,column=1)
        tk.Entry(self.page,textvariable = self.username).grid(row = 1,column=2) #textvariable，将输入框与变量绑定，若修改则会一起修改
        # pady-间隔
        tk.Label(self.page, text = '密码: ').grid(row = 2,column=1,pady = 10)
        tk.Entry(self.page,textvariable = self.password).grid(row = 2,column=2)

        tk.Button(self.page, text = '登陆',command = self.login).grid(row = 3,column = 1,pady = 10)
        tk.Button(self.page, text = '退出',command=self.page.quit).grid(row = 3,column = 2) #quit:tkinder中用来退出事件

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        # flag接受第一个值（布尔值），message接收第二个值（字符串）
        flag, message = db.check_login(name,pwd)
        if flag:
            self.page.destroy() # 删除一整个框架
            MianPage(self.root)

        else:
            messagebox.showwarning(title = '警告',message = message)



if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master = root)
    root.mainloop()
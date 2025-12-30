# bank_gui.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

class BankLoginGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("银行管理系统 - 登录")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        # 设置背景色
        self.window.configure(bg='#f0f0f0')
        
        self.create_widgets()
    
    def create_widgets(self):
        # 标题
        title_label = tk.Label(
            self.window, 
            text="银行管理系统",
            font=("微软雅黑", 24, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=30)
        
        # 分隔线
        separator = tk.Frame(self.window, height=2, bg='#3498db')
        separator.pack(fill='x', padx=50, pady=5)
        
        # 管理员账户标签和输入框
        user_frame = tk.Frame(self.window, bg='#f0f0f0')
        user_frame.pack(pady=10)
        
        tk.Label(
            user_frame,
            text="管理员账户:",
            font=("微软雅黑", 12),
            bg='#f0f0f0'
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.user_entry = tk.Entry(
            user_frame,
            font=("微软雅黑", 12),
            width=15
        )
        self.user_entry.pack(side=tk.LEFT)
        
        # 密码标签和输入框
        password_frame = tk.Frame(self.window, bg='#f0f0f0')
        password_frame.pack(pady=10)
        
        tk.Label(
            password_frame,
            text="密　　码:",
            font=("微软雅黑", 12),
            bg='#f0f0f0'
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.password_entry = tk.Entry(
            password_frame,
            font=("微软雅黑", 12),
            width=15,
            show="*"  # 密码显示为*
        )
        self.password_entry.pack(side=tk.LEFT)
        
        # 按钮框架
        button_frame = tk.Frame(self.window, bg='#f0f0f0')
        button_frame.pack(pady=30)
        
        # 登录按钮
        login_btn = tk.Button(
            button_frame,
            text="登录",
            font=("微软雅黑", 12, "bold"),
            bg='#3498db',
            fg='white',
            width=10,
            height=2,
            command=self.login,
            cursor="hand2"  # 鼠标悬停时变成手型
        )
        login_btn.pack(side=tk.LEFT, padx=10)
        
        # 退出按钮
        exit_btn = tk.Button(
            button_frame,
            text="退出",
            font=("微软雅黑", 12, "bold"),
            bg='#e74c3c',
            fg='white',
            width=10,
            height=2,
            command=self.exit_system,
            cursor="hand2"
        )
        exit_btn.pack(side=tk.LEFT, padx=10)
    
    # 在 bank_gui.py 的 login() 方法中修改：
    def login(self):
        """验证登录信息"""
        username = self.user_entry.get()
        password = self.password_entry.get()
        
        # 管理员账户和密码
        admin_username = "admin"
        admin_password = "12345"
        
        if username == admin_username and password == admin_password:
            messagebox.showinfo("登录成功", "登录成功！")
            self.window.destroy()  # 关闭登录窗口
            
            # 打开角色选择界面
            try:
                from role_selector import RoleSelector
                selector = RoleSelector()
                selector.run()
            except ImportError:
                # 如果没有角色选择界面，直接进入银行系统
                self.run_command_line()
        else:
            messagebox.showerror("登录失败", "管理员账户或密码错误！")
    def exit_system(self):
        """退出系统"""
        if messagebox.askyesno("确认退出", "确定要退出银行管理系统吗？"):
            self.window.destroy()
    
    def run(self):
        """运行GUI"""
        self.window.mainloop()

# 程序入口
if __name__ == "__main__":
    app = BankLoginGUI()
    app.run()
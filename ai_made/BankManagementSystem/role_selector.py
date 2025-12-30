import tkinter as tk
from tkinter import messagebox
import sys

class RoleSelector:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("银行管理系统 - 角色选择")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.window.configure(bg='#f0f0f0')
        
        # 居中显示
        self.center_window()
        
        self.create_widgets()
    
    def center_window(self):
        """窗口居中显示"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # 标题
        tk.Label(
            self.window, 
            text="请选择角色",
            font=("微软雅黑", 18),
            bg='#f0f0f0'
        ).pack(pady=20)
        
        # 管理员功能按钮
        tk.Button(
            self.window, 
            text="管理员功能",
            font=("微软雅黑", 14),
            bg='#3498db',
            fg='white',
            width=15,
            height=2,
            command=self.open_admin_system
        ).pack(pady=15)
        
        # 客户功能按钮
        tk.Button(
            self.window, 
            text="客户功能",
            font=("微软雅黑", 14),
            bg='#2ecc71',
            fg='white',
            width=15,
            height=2,
            command=self.open_customer_system
        ).pack(pady=15)
        
        # 退出按钮
        tk.Button(
            self.window, 
            text="退出系统",
            font=("微软雅黑", 10),
            bg='#e74c3c',
            fg='white',
            width=10,
            command=self.exit_system
        ).pack(pady=20)
    
    def open_admin_system(self):
        """打开管理员系统"""
        self.window.destroy()  # 关闭角色选择窗口
        
        try:
            from admin_simple import AdminSimpleGUI
            admin_gui = AdminSimpleGUI()
            admin_gui.run()
        except ImportError as e:
            messagebox.showerror("错误", "无法启动管理员界面")
            sys.exit(1)
    
    def open_customer_system(self):
        """打开客户系统"""
        self.window.destroy()  # 关闭角色选择窗口
        
        try:
            from bank_main import Bank
            bank = Bank()
            from customer_gui import CustomerGUI
            customer_gui = CustomerGUI(bank)
            customer_gui.run()
        except ImportError as e:
            messagebox.showerror("错误", "无法启动客户系统")
            sys.exit(1)
    
    def exit_system(self):
        """退出系统"""
        if messagebox.askyesno("确认退出", "确定要退出银行管理系统吗？"):
            self.window.destroy()
            sys.exit(0)
    
    def run(self):
        """运行GUI"""
        self.window.mainloop()

if __name__ == "__main__":
    app = RoleSelector()
    app.run()

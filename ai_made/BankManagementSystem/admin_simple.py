# admin_simple.py - 极简管理员界面（只有退出功能）
import tkinter as tk
from tkinter import messagebox
import sys

class AdminSimpleGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("银行管理系统 - 管理员")
        self.window.geometry("300x200")
        self.window.configure(bg='#f0f0f0')
        
        # 设置窗口居中
        self.center_window(300, 200)
        
        self.create_widgets()
    
    def center_window(self, width, height):
        """窗口居中显示"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # 欢迎文字
        welcome_label = tk.Label(
            self.window,
            text="欢迎，管理员",
            font=("微软雅黑", 18, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        welcome_label.pack(pady=40)
        
        # 退出按钮
        exit_btn = tk.Button(
            self.window,
            text="退出程序",
            font=("微软雅黑", 14, "bold"),
            bg='#e74c3c',
            fg='white',
            width=15,
            height=2,
            command=self.confirm_exit,
            cursor="hand2"
        )
        exit_btn.pack(pady=10)
        
        # 提示文字
        tip_label = tk.Label(
            self.window,
            text="点击按钮退出系统",
            font=("微软雅黑", 10),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        tip_label.pack(pady=10)
    
    def confirm_exit(self):
        """确认退出程序"""
        if messagebox.askyesno("确认退出", "确定要退出银行管理系统吗？"):
            self.window.destroy()
            sys.exit(0)  # 完全退出程序
    
    def run(self):
        """运行GUI"""
        self.window.mainloop()

if __name__ == "__main__":
    app = AdminSimpleGUI()
    app.run()
# customer_gui.py - 客户功能界面（带菜单栏）
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random
import sys
from datetime import datetime

class CustomerGUI:
    def __init__(self, bank_instance):
        self.bank = bank_instance
        self.window = tk.Tk()
        self.window.title("银行管理系统 - 客户功能")
        self.window.geometry("800x600")
        self.window.configure(bg='#f0f0f0')
        
        # 设置窗口图标（可选）
        try:
            self.window.iconbitmap('bank.ico')  # 如果有图标文件
        except:
            pass
        
        # 设置窗口居中
        self.center_window(800, 600)
        
        # 设置窗口关闭事件
        self.window.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        
        self.create_menu()
        self.create_widgets()
    
    def center_window(self, width, height):
        """窗口居中显示"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        # 账户管理菜单
        account_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="账户管理", menu=account_menu)
        account_menu.add_command(label="开户", command=self.open_account, accelerator="Ctrl+N")
        account_menu.add_separator()
        account_menu.add_command(label="查询余额", command=self.check_balance)
        account_menu.add_separator()
        account_menu.add_command(label="取款", command=self.withdraw_money)
        account_menu.add_command(label="存款", command=self.deposit_money)
        account_menu.add_command(label="转账", command=self.transfer_money)
        account_menu.add_separator()
        account_menu.add_command(label="锁定账户", command=self.lock_account)
        
        # 工具菜单
        tool_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="工具", menu=tool_menu)
        tool_menu.add_command(label="查看交易记录", command=self.show_transactions)
        tool_menu.add_separator()
        tool_menu.add_command(label="修改密码", command=self.change_password)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="使用说明", command=self.show_help)
        help_menu.add_separator()
        help_menu.add_command(label="关于", command=self.show_about)
        
        # 退出菜单
        exit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="退出", menu=exit_menu)
        exit_menu.add_command(label="退出系统", command=self.confirm_exit, accelerator="Ctrl+Q")
        
        # 绑定快捷键
        self.window.bind('<Control-n>', lambda e: self.open_account())
        self.window.bind('<Control-q>', lambda e: self.confirm_exit())
    
    def create_widgets(self):
        """创建主界面组件"""
        # 标题区域
        title_frame = tk.Frame(self.window, bg='#2c3e50', height=100)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="银行客户服务系统",
            font=("微软雅黑", 28, "bold"),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(
            title_frame,
            text="请从菜单栏选择操作",
            font=("微软雅黑", 12),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        subtitle_label.pack(pady=(0, 10))
        
        # 主内容区域
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # 左侧功能快捷面板
        left_frame = tk.Frame(main_frame, bg='#f0f0f0', width=200)
        left_frame.pack(side='left', fill='y', padx=(0, 20))
        left_frame.pack_propagate(False)
        
        tk.Label(
            left_frame,
            text="快捷功能",
            font=("微软雅黑", 14, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=(0, 15))
        
        # 快捷功能按钮
        quick_buttons = [
            ("💰 开户", self.open_account),
            ("📊 查询", self.check_balance),
            ("💸 取款", self.withdraw_money),
            ("💰 存款", self.deposit_money),
            ("🔄 转账", self.transfer_money),
            ("🔒 锁定", self.lock_account),
        ]
        
        for text, command in quick_buttons:
            btn = tk.Button(
                left_frame,
                text=text,
                font=("微软雅黑", 11),
                bg='#3498db',
                fg='white',
                width=15,
                height=2,
                command=command,
                cursor="hand2"
            )
            btn.pack(pady=5)
        
        # 右侧信息显示区域
        right_frame = tk.Frame(main_frame, bg='white')
        right_frame.pack(side='right', fill='both', expand=True)
        
        # 创建记事本风格的信息显示区
        self.info_text = tk.Text(
            right_frame,
            wrap=tk.WORD,
            font=("微软雅黑", 11),
            bg='white',
            fg='black',
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        
        # 添加滚动条
        scrollbar = tk.Scrollbar(right_frame, command=self.info_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.info_text.config(yscrollcommand=scrollbar.set)
        self.info_text.pack(fill='both', expand=True)
        
        # 添加欢迎信息
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        welcome_msg = f"""
        {'='*60}
        欢迎使用银行客户服务系统！
        当前时间: {current_time}
        {'='*60}
        
        请从菜单栏或左侧快捷按钮选择操作：
        
        1. 开户 - 创建新的银行账户
        2. 查询 - 查看账户余额
        3. 取款 - 从账户取款
        4. 存款 - 向账户存款
        5. 转账 - 向其他账户转账
        6. 锁定 - 锁定您的账户
        
        提示：按 Ctrl+N 快速开户，按 Ctrl+Q 退出系统。
        """
        self.info_text.insert(tk.END, welcome_msg)
        self.info_text.config(state='disabled')  # 设置为只读
        
        # 状态栏
        status_frame = tk.Frame(self.window, bg='#ecf0f1', height=30)
        status_frame.pack(fill='x', side='bottom')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="就绪 | 请选择操作",
            font=("微软雅黑", 9),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.status_label.pack(side='left', padx=10)
        
        # 时间显示
        self.time_label = tk.Label(
            status_frame,
            text=current_time,
            font=("微软雅黑", 9),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        self.time_label.pack(side='right', padx=10)
        
        # 更新时间显示
        self.update_time()
    
    def update_time(self):
        """更新时间显示"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        self.window.after(1000, self.update_time)  # 每秒更新一次
    
    def open_account(self):
        """开户功能"""
        self.info_text.config(state='normal')
        self.info_text.delete(1.0, tk.END)
        
        # 创建开户对话框
        dialog = tk.Toplevel(self.window)
        dialog.title("开户")
        dialog.geometry("400x450")
        dialog.configure(bg='#f0f0f0')
        dialog.transient(self.window)
        dialog.grab_set()
        
        # 居中显示
        dialog.update_idletasks()
        x = (self.window.winfo_screenwidth() - dialog.winfo_width()) // 2
        y = (self.window.winfo_screenheight() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
        
        tk.Label(dialog, text="开户信息", font=("微软雅黑", 16, "bold"), bg='#f0f0f0').pack(pady=10)
        
        # 创建输入框
        fields = [
            ("姓名:", "entry"),
            ("身份证号:", "entry"),
            ("手机号:", "entry"),
            ("预存金额:", "entry"),
            ("密码:", "entry", {"show": "*"}),
            ("确认密码:", "entry", {"show": "*"})
        ]
        
        entries = {}
        for i, (label, entry_type, *kwargs) in enumerate(fields):
            frame = tk.Frame(dialog, bg='#f0f0f0')
            frame.pack(pady=5, padx=20, fill='x')
            
            tk.Label(frame, text=label, width=10, anchor='w', bg='#f0f0f0').pack(side='left')
            
            if entry_type == "entry":
                kwargs_dict = kwargs[0] if kwargs else {}
                entry = tk.Entry(frame, width=25, **kwargs_dict)
                entry.pack(side='right', fill='x', expand=True)
                entries[label] = entry
        
        result_label = tk.Label(dialog, text="", bg='#f0f0f0', fg='red')
        result_label.pack(pady=10)
        
        def submit():
            # 获取输入值
            try:
                name = entries["姓名:"].get()
                id_number = entries["身份证号:"].get()
                phone = entries["手机号:"].get()
                money = entries["预存金额:"].get()
                password = entries["密码:"].get()
                confirm_password = entries["确认密码:"].get()
                
                # 验证输入
                if not all([name, id_number, phone, money, password]):
                    result_label.config(text="请填写所有字段！")
                    return
                
                if password != confirm_password:
                    result_label.config(text="两次输入的密码不一致！")
                    return
                
                try:
                    phone = int(phone)
                    money = int(money)
                    if money < 0:
                        result_label.config(text="预存金额不能为负数！")
                        return
                except ValueError:
                    result_label.config(text="手机号和金额必须是数字！")
                    return
                
                # 生成卡号
                while True:
                    card_id = str(random.randint(100000, 999999))
                    if card_id not in self.bank.dict:
                        break
                
                # 创建账户信息
                info = {
                    "姓名": name,
                    "身份证号": id_number,
                    "手机号": phone,
                    "金额": money,
                    "密码": password
                }
                
                # 保存到银行系统
                self.bank.dict[card_id] = info
                self.bank.save_file()
                
                # 显示成功信息
                success_msg = f"""
                {'='*50}
                开户成功！
                {'='*50}
                卡号：{card_id}
                姓名：{name}
                身份证号：{id_number}
                手机号：{phone}
                余额：{money}元
                {'='*50}
                重要提示：请牢记您的卡号和密码！
                """
                self.info_text.insert(tk.END, success_msg)
                self.info_text.config(state='disabled')
                
                # 记录交易
                self.log_transaction(card_id, "开户", money, money)
                
                dialog.destroy()
                self.update_status("开户成功")
                messagebox.showinfo("开户成功", f"开户成功！\n您的卡号是：{card_id}\n请妥善保管！")
                
            except Exception as e:
                result_label.config(text=f"开户失败：{str(e)}")
        
        # 按钮区域
        button_frame = tk.Frame(dialog, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="提交", command=submit, bg='#3498db', fg='white', width=10).pack(side='left', padx=10)
        tk.Button(button_frame, text="取消", command=dialog.destroy, bg='#95a5a6', fg='white', width=10).pack(side='left', padx=10)
    
    def check_balance(self):
        """查询余额"""
        card_id = simpledialog.askstring("查询余额", "请输入卡号：", parent=self.window)
        if not card_id:
            return
        
        if card_id not in self.bank.dict:
            messagebox.showerror("错误", "卡号不存在！")
            return
        
        if card_id in self.bank.lock_dict:
            messagebox.showerror("错误", "该账户已被锁定！")
            return
        
        # 验证密码
        password = simpledialog.askstring("验证密码", "请输入密码：", parent=self.window, show='*')
        if password != self.bank.dict[card_id]["密码"]:
            messagebox.showerror("错误", "密码错误！")
            return
        
        info = self.bank.dict[card_id]
        balance_msg = f"""
        {'='*50}
        账户信息查询
        {'='*50}
        卡号：{card_id}
        姓名：{info['姓名']}
        余额：{info['金额']}元
        状态：{'🔒 已锁定' if card_id in self.bank.lock_dict else '✅ 正常'}
        {'='*50}
        """
        
        self.info_text.config(state='normal')
        self.info_text.insert(tk.END, balance_msg)
        self.info_text.config(state='disabled')
        self.info_text.see(tk.END)
        
        self.update_status("查询成功")
        messagebox.showinfo("查询结果", f"余额：{info['金额']}元")
    
    def withdraw_money(self):
        """取款功能"""
        card_id = simpledialog.askstring("取款", "请输入卡号：", parent=self.window)
        if not card_id:
            return
        
        if card_id not in self.bank.dict:
            messagebox.showerror("错误", "卡号不存在！")
            return
        
        if card_id in self.bank.lock_dict:
            messagebox.showerror("错误", "该账户已被锁定！")
            return
        
        # 验证密码
        password = simpledialog.askstring("验证密码", "请输入密码：", parent=self.window, show='*')
        if password != self.bank.dict[card_id]["密码"]:
            messagebox.showerror("错误", "密码错误！")
            return
        
        # 输入取款金额
        try:
            amount = simpledialog.askinteger("取款金额", "请输入取款金额：", parent=self.window, minvalue=1)
            if not amount:
                return
            
            if amount > self.bank.dict[card_id]["金额"]:
                messagebox.showerror("错误", "余额不足！")
                return
            
            # 确认取款
            confirm = messagebox.askyesno("确认取款", f"确定取款 {amount} 元吗？")
            if not confirm:
                return
            
            # 执行取款
            old_balance = self.bank.dict[card_id]["金额"]
            self.bank.dict[card_id]["金额"] = old_balance - amount
            self.bank.save_file()
            
            # 记录交易
            self.log_transaction(card_id, "取款", -amount, old_balance - amount)
            
            # 显示结果
            result_msg = f"""
            {'='*50}
            取款成功！
            {'='*50}
            卡号：{card_id}
            取款金额：{amount}元
            原余额：{old_balance}元
            新余额：{self.bank.dict[card_id]['金额']}元
            时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*50}
            """
            
            self.info_text.config(state='normal')
            self.info_text.insert(tk.END, result_msg)
            self.info_text.config(state='disabled')
            self.info_text.see(tk.END)
            
            self.update_status("取款成功")
            messagebox.showinfo("取款成功", f"取款 {amount} 元成功！\n当前余额：{self.bank.dict[card_id]['金额']}元")
            
        except Exception as e:
            messagebox.showerror("错误", f"取款失败：{str(e)}")
    
    def deposit_money(self):
        """存款功能"""
        card_id = simpledialog.askstring("存款", "请输入卡号：", parent=self.window)
        if not card_id:
            return
        
        if card_id not in self.bank.dict:
            messagebox.showerror("错误", "卡号不存在！")
            return
        
        if card_id in self.bank.lock_dict:
            messagebox.showerror("错误", "该账户已被锁定！")
            return
        
        # 验证密码
        password = simpledialog.askstring("验证密码", "请输入密码：", parent=self.window, show='*')
        if password != self.bank.dict[card_id]["密码"]:
            messagebox.showerror("错误", "密码错误！")
            return
        
        # 输入存款金额
        try:
            amount = simpledialog.askinteger("存款金额", "请输入存款金额：", parent=self.window, minvalue=1)
            if not amount:
                return
            
            # 确认存款
            confirm = messagebox.askyesno("确认存款", f"确定存款 {amount} 元吗？")
            if not confirm:
                return
            
            # 执行存款
            old_balance = self.bank.dict[card_id]["金额"]
            self.bank.dict[card_id]["金额"] = old_balance + amount
            self.bank.save_file()
            
            # 记录交易
            self.log_transaction(card_id, "存款", amount, old_balance + amount)
            
            # 显示结果
            result_msg = f"""
            {'='*50}
            存款成功！
            {'='*50}
            卡号：{card_id}
            存款金额：{amount}元
            原余额：{old_balance}元
            新余额：{self.bank.dict[card_id]['金额']}元
            时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*50}
            """
            
            self.info_text.config(state='normal')
            self.info_text.insert(tk.END, result_msg)
            self.info_text.config(state='disabled')
            self.info_text.see(tk.END)
            
            self.update_status("存款成功")
            messagebox.showinfo("存款成功", f"存款 {amount} 元成功！\n当前余额：{self.bank.dict[card_id]['金额']}元")
            
        except Exception as e:
            messagebox.showerror("错误", f"存款失败：{str(e)}")
    
    def transfer_money(self):
        """转账功能"""
        # 输入转出卡号
        from_card = simpledialog.askstring("转账", "请输入您的卡号：", parent=self.window)
        if not from_card:
            return
        
        if from_card not in self.bank.dict:
            messagebox.showerror("错误", "卡号不存在！")
            return
        
        if from_card in self.bank.lock_dict:
            messagebox.showerror("错误", "您的账户已被锁定！")
            return
        
        # 验证密码
        password = simpledialog.askstring("验证密码", "请输入密码：", parent=self.window, show='*')
        if password != self.bank.dict[from_card]["密码"]:
            messagebox.showerror("错误", "密码错误！")
            return
        
        # 输入转入卡号
        to_card = simpledialog.askstring("转账", "请输入对方卡号：", parent=self.window)
        if not to_card:
            return
        
        if to_card not in self.bank.dict:
            messagebox.showerror("错误", "对方卡号不存在！")
            return
        
        if to_card == from_card:
            messagebox.showerror("错误", "不能转账给自己！")
            return
        
        # 输入转账金额
        try:
            amount = simpledialog.askinteger("转账金额", "请输入转账金额：", parent=self.window, minvalue=1)
            if not amount:
                return
            
            if amount > self.bank.dict[from_card]["金额"]:
                messagebox.showerror("错误", "余额不足！")
                return
            
            # 显示转账信息并确认
            info = f"""
            转账信息：
            转出卡号：{from_card}
            转入卡号：{to_card}
            转账金额：{amount}元
            转出账户余额：{self.bank.dict[from_card]['金额']}元
            """
            
            confirm = messagebox.askyesno("确认转账", info)
            if not confirm:
                return
            
            # 执行转账
            from_old = self.bank.dict[from_card]["金额"]
            to_old = self.bank.dict[to_card]["金额"]
            
            self.bank.dict[from_card]["金额"] = from_old - amount
            self.bank.dict[to_card]["金额"] = to_old + amount
            self.bank.save_file()
            
            # 记录交易
            self.log_transaction(from_card, "转账转出", -amount, from_old - amount)
            self.log_transaction(to_card, "转账转入", amount, to_old + amount)
            
            # 显示结果
            result_msg = f"""
            {'='*50}
            转账成功！
            {'='*50}
            转出卡号：{from_card}
            转入卡号：{to_card}
            转账金额：{amount}元
            转出账户新余额：{self.bank.dict[from_card]['金额']}元
            时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*50}
            """
            
            self.info_text.config(state='normal')
            self.info_text.insert(tk.END, result_msg)
            self.info_text.config(state='disabled')
            self.info_text.see(tk.END)
            
            self.update_status("转账成功")
            messagebox.showinfo("转账成功", f"转账 {amount} 元成功！\n您的余额：{self.bank.dict[from_card]['金额']}元")
            
        except Exception as e:
            messagebox.showerror("错误", f"转账失败：{str(e)}")
    
    def lock_account(self):
        """锁定账户"""
        card_id = simpledialog.askstring("锁定账户", "请输入卡号：", parent=self.window)
        if not card_id:
            return
        
        if card_id not in self.bank.dict:
            messagebox.showerror("错误", "卡号不存在！")
            return
        
        if card_id in self.bank.lock_dict:
            messagebox.showerror("错误", "该账户已被锁定！")
            return
        
        # 验证密码
        password = simpledialog.askstring("验证密码", "请输入密码：", parent=self.window, show='*')
        if password != self.bank.dict[card_id]["密码"]:
            messagebox.showerror("错误", "密码错误！")
            return
        
        # 确认锁定
        confirm = messagebox.askyesno("确认锁定", "确定要锁定账户吗？\n锁定后无法进行任何操作！")
        if not confirm:
            return
        
        # 执行锁定
        self.bank.lock_dict[card_id] = self.bank.dict[card_id]
        self.bank.save_file()
        
        result_msg = f"""
        {'='*50}
        账户锁定成功！
        {'='*50}
        卡号：{card_id}
        锁定时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        状态：已锁定 🔒
        提示：请联系管理员解锁账户
        {'='*50}
        """
        
        self.info_text.config(state='normal')
        self.info_text.insert(tk.END, result_msg)
        self.info_text.config(state='disabled')
        self.info_text.see(tk.END)
        
        self.update_status("账户锁定成功")
        messagebox.showinfo("锁定成功", "账户已锁定！")
    
    def show_transactions(self):
        """查看交易记录"""
        # 这里可以扩展为读取交易日志文件
        messagebox.showinfo("交易记录", "交易记录功能开发中...")
    
    def change_password(self):
        """修改密码"""
        messagebox.showinfo("修改密码", "密码修改功能开发中...")
    
    def show_help(self):
        """显示帮助"""
        help_text = """
        银行客户服务系统使用说明
        
        菜单功能：
        1. 账户管理 - 包含所有账户操作
        2. 工具 - 其他辅助功能
        3. 帮助 - 使用说明和关于信息
        4. 退出 - 退出系统
        
        快捷键：
        Ctrl+N - 快速开户
        Ctrl+Q - 快速退出
        
        如有问题，请联系系统管理员。
        """
        messagebox.showinfo("使用说明", help_text)
    
    def show_about(self):
        """显示关于信息"""
        about_text = """
        银行管理系统
        
        版本：1.0
        开发：银行科技部
        日期：2024年
        
        功能：开户、查询、取款、存款、转账、锁定
        
        版权所有 © 2024
        """
        messagebox.showinfo("关于", about_text)
    
    def log_transaction(self, card_id, operation, amount, new_balance):
        """记录交易（简化版）"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} | 卡号:{card_id} | 操作:{operation} | 金额:{amount} | 余额:{new_balance}\n"
            
            # 记录到文本区域
            self.info_text.config(state='normal')
            self.info_text.insert(tk.END, f"[交易记录] {log_entry}")
            self.info_text.config(state='disabled')
            self.info_text.see(tk.END)
            
            # 也可以保存到文件
            with open("transaction_log.txt", "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"记录交易失败：{e}")
    
    def update_status(self, message):
        """更新状态栏"""
        self.status_label.config(text=f"状态: {message}")
    
    def confirm_exit(self):
        """确认退出程序"""
        confirm = messagebox.askyesno("确认退出", "确定要退出银行管理系统吗？")
        if confirm:
            self.window.destroy()
            sys.exit(0)
    
    def run(self):
        """运行GUI"""
        self.window.mainloop()

if __name__ == "__main__":
    # 测试代码
    from bank_main import Bank
    bank = Bank()
    app = CustomerGUI(bank)
    app.run()
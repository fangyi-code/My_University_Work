import json
import datetime 
import tkinter as tk
from tkinter import messagebox,ttk

# #json文件中键必须用双引号，如果值是字符串，那也要用双引号
# d = '[{"时间":"2022/05/07 14:20:21","项目":"收到货款","金额":20000,"分类":"收入"}]'
# with open (r"data.txt","w") as f:
#     f.write(d)

# 读取数据函数
def readData():
    try:
        with open (r"data.txt","r") as f:
            # f.read得到json字符串（符合json格式）
            jsonData = f.read()
            # json.loads()得到python对象
            dataList = json.loads(jsonData)
            return dataList
    except FileNotFoundError:
        # 如果文件不存在，返回空列表
        return []
    except json.JSONDecodeError:
        # 如果JSON格式错误，返回空列表
        return []
    except Exception as e:
        # 其他异常，返回空列表
        return []

def writeData(dataList):
    try:
        # 将python对象转化为json字符串
        jsonData = json.dumps(dataList, ensure_ascii=False)
        with open(f"data.txt","w", encoding='utf-8') as f:
            f.write(jsonData)
        return True  # 写入成功
    except Exception as e:
        # 如果写入失败，返回False，错误信息由调用方处理
        return False


def showData():
    data = readData()
    return [
        [d["时间"], d["项目"], d["金额"] if d["分类"] == "收入" else d["金额"]*-1, d["分类"]]
        for d in data
    ]

def sumin():
    sumin = 0
    data = readData()
    for d in data:
        if d["分类"] == "收入":
            sumin += d["金额"]
    return sumin

def sumout():
    sumout = 0
    data = readData()
    for d in data:
        if d["分类"] == "支出":
            sumout += d["金额"]
    return sumout

# 数据验证函数
def validate_input(project, amount_str):
    """
    验证输入数据
    参数:
        project: 项目名称
        amount_str: 金额字符串
    返回:
        (is_valid, error_message, amount)
        is_valid: 是否有效
        error_message: 错误信息（如果无效）
        amount: 转换后的金额（如果有效）
    """
    # 验证项目名称不能为空
    if not project or not project.strip():
        return False, "项目名称不能为空！", None
    
    # 验证金额不能为空
    if not amount_str or not amount_str.strip():
        return False, "金额不能为空！", None
    
    # 验证金额必须是数字
    try:
        amount = float(amount_str)
    except ValueError:
        return False, "金额必须是数字！", None
    
    # 验证金额不能为负数
    if amount < 0:
        return False, "金额不能为负数！", None
    
    # 验证金额不能为0（可选，根据需求决定）
    if amount == 0:
        return False, "金额不能为0！", None
    
    return True, "", amount

 # 增加数据
def addData(content,amount,cla):
    try:
        dataList = readData()
        t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        data = {"时间":t,"项目":content,"金额":amount,"分类":cla}
        dataList.append(data)
        if not writeData(dataList):
            raise Exception("保存数据失败")
    except Exception as e:
        raise Exception(f"添加数据失败：{str(e)}")

# 删除数据
def deleteData(index):
    try:
        dataList = readData()
        if 0 <= index < len(dataList):
            dataList.pop(index)
            if not writeData(dataList):
                raise Exception("保存数据失败")
        else:
            raise Exception("索引超出范围")
    except Exception as e:
        raise Exception(f"删除数据失败：{str(e)}")

# 编辑数据
def editData(index, content, amount, cla):
    try:
        dataList = readData()
        if 0 <= index < len(dataList):
            # 保留原时间，只更新项目、金额、分类
            dataList[index]["项目"] = content
            dataList[index]["金额"] = amount
            dataList[index]["分类"] = cla
            if not writeData(dataList):
                raise Exception("保存数据失败")
        else:
            raise Exception("索引超出范围")
    except Exception as e:
        raise Exception(f"编辑数据失败：{str(e)}")

def main():
    # 创建主窗口对象，命名记账本
    window = tk.Tk()
    window.title("记账本")
    
    # 帐目清单
    tk.Label(window, text="帐目清单: ").pack()
    
    # 表格
    tree = ttk.Treeview(window, columns=("时间","项目","金额","分类"), show="headings", height=10)
    tree.heading("时间", text="时间")
    tree.heading("项目", text="项目")
    tree.heading("金额", text="金额")
    tree.heading("分类", text="分类")
    tree.pack()
    
    # 统计信息
    summary_label = tk.Label(window, text="总收入多少元，总支出多少元，结余多少元，双击可修改数据。")
    summary_label.pack()

 
    # 输入项目
    frame1 = tk.Frame(window)
    frame1.pack()
    tk.Label(frame1, text="请输入帐单项目: ").pack(side=tk.LEFT)
    # Entry是输入框
    entry_project = tk.Entry(frame1)
    entry_project.pack(side=tk.LEFT)
    
    # 输入金额
    frame2 = tk.Frame(window)
    frame2.pack()
    tk.Label(frame2, text="请输入帐单金额: ").pack(side=tk.LEFT)
    entry_amount = tk.Entry(frame2)
    entry_amount.pack(side=tk.LEFT)

 
    # 选择分类
    frame3 = tk.Frame(window)
    frame3.pack()
    tk.Label(frame3, text="请选择帐单分类: ").pack(side=tk.LEFT)
    # 创建一个收入支出共享的变量，默认收入
    category_var = tk.StringVar(value="收入")
    tk.Radiobutton(frame3, text="收入", variable=category_var, value="收入").pack(side=tk.LEFT)
    tk.Radiobutton(frame3, text="支出", variable=category_var, value="支出").pack(side=tk.LEFT)

    def refresh_display():
        # 更新表格
        for item in tree.get_children():
            tree.delete(item)
        data = showData()
        for row in data:
            tree.insert("", tk.END, values=row)
        
        # 更新统计
        total_in = sumin()
        total_out = sumout()
        balance = total_in - total_out
        summary_label.config(text=f"总收入{total_in}元，总支出{total_out}元，结余{balance}元，双击可修改数据。")
        
  # 确认提交
    def submit():
        try:
            # tkinter控件对象必须使用get()来获取值
            project = entry_project.get()
            amount_str = entry_amount.get()
            category = category_var.get()
            
            # 数据验证
            is_valid, error_message, amount = validate_input(project, amount_str)
            if not is_valid:
                messagebox.showwarning('输入错误', error_message)
                return  # 验证失败，提前退出
            
            # 验证通过，添加数据
            addData(project, amount, category)
            refresh_display()
            
            # 清空输入框
            entry_project.delete(0, tk.END)
            entry_amount.delete(0, tk.END)
            
            messagebox.showinfo('成功', '账单添加成功！')
        except Exception as e:
            # 捕获所有异常（包括数据验证和文件操作异常）
            messagebox.showerror('错误', f'发生错误：{str(e)}')
    
    # 删除选中
    def delete_selected():
        try:
            # 存储当前选中的行（内部id）
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('警告', '请先选择要删除的记录！')
                return
            
            # 对话框标题与询问内容，点击yes返回true，no返回false
            if messagebox.askyesno('确认', '确定要删除这条记录吗？'):
                item = selected[0]
                # 将 Treeview 的行标识符转换为行号（索引）
                index = tree.index(item)
                deleteData(index)
                refresh_display()
                messagebox.showinfo('成功', '账单删除成功！')
        except Exception as e:
            # 捕获所有异常（包括文件操作异常）
            messagebox.showerror('错误', f'删除失败：{str(e)}')
            
        
    # 编辑选中
    def edit_selected():
        # 获取内部id
        selected = tree.selection()
        if not selected:
            messagebox.showwarning('警告', '请先选择要编辑的记录！')
            return
        # 获取第一个内部id
        item = selected[0]
        # 将第一个内部id转换为索引
        index = tree.index(item)
        dataList = readData()
        if 0 <= index < len(dataList):
            old_data = dataList[index]
            
            # 创建编辑窗口
            edit_window = tk.Toplevel(window)# 创建子窗口（弹出窗口）
            edit_window.title("编辑记录")
            edit_window.geometry("300x200")# 设置窗口大小（宽x高）
            
            # 创建输入控件并预填充数据
            # 项目输入
            tk.Label(edit_window, text="项目:").pack(pady=5)
            entry_edit_project = tk.Entry(edit_window, width=30)# 创建输入框
            entry_edit_project.insert(0, old_data["项目"])# 在位置0插入原项目名（预填充）
            entry_edit_project.pack(pady=5)
            
            # 金额输入
            tk.Label(edit_window, text="金额:").pack(pady=5)
            entry_edit_amount = tk.Entry(edit_window, width=30)
            entry_edit_amount.insert(0, str(old_data["金额"]))
            entry_edit_amount.pack(pady=5)
            
            # 分类
            tk.Label(edit_window, text="分类:").pack(pady=5)
            edit_category_var = tk.StringVar(value=old_data["分类"])# 创建变量，初始值为原分类
            frame_edit_category = tk.Frame(edit_window)
            frame_edit_category.pack(pady=5)
            tk.Radiobutton(frame_edit_category, text="收入", variable=edit_category_var, value="收入").pack(side=tk.LEFT, padx=10)
            tk.Radiobutton(frame_edit_category, text="支出", variable=edit_category_var, value="支出").pack(side=tk.LEFT, padx=10)
            # 确认按钮
            def confirm_edit():
                try:
                    project = entry_edit_project.get()
                    amount_str = entry_edit_amount.get()
                    category = edit_category_var.get()
                    
                    # 数据验证
                    is_valid, error_message, amount = validate_input(project, amount_str)
                    if not is_valid:
                        messagebox.showwarning('输入错误', error_message)
                        return  # 验证失败，提前退出
                    
                    # 验证通过，保存数据
                    editData(index, project, amount, category)
                    refresh_display()
                    edit_window.destroy()
                    messagebox.showinfo('成功', '账单编辑成功！')
                except Exception as e:
                    # 捕获所有异常（包括数据验证和文件操作异常）
                    messagebox.showerror('错误', f'发生错误：{str(e)}')
            
            tk.Button(edit_window, text="确认", command=confirm_edit).pack(pady=10)
    
    # 双击编辑
    def on_double_click(event):
        edit_selected()
    
    # 绑定双击事件
    # double-1 鼠标左键双击，bind（）绑定事件
    tree.bind("<Double-1>", on_double_click)     


    # 按钮框架
    frame_buttons = tk.Frame(window)
    # pack布局管理器
    # pady = 10:设置上下边距为10像素
    frame_buttons.pack(pady=10)
    
    # 创建按钮对象，父容器frame_buttons，文本为"确认提交"，点击时调用submit/delete_selected函数
    tk.Button(frame_buttons, text="确认提交", command=submit).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_buttons, text="删除选中", command=delete_selected).pack(side=tk.LEFT, padx=5)
    
    # 初始化数据
    refresh_display()
    
    # 让窗口保持运行
    window.mainloop()

main()

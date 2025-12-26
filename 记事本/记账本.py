import json
import datetime 
import tkinter as tk
from tkinter import messagebox,ttk

#json文件中键必须用双引号，如果值是字符串，那也要用双引号
# d = '[{"时间":"2022/05/07 14:20:21","项目":"收到货款","金额":20000,"分类":"收入"}]'
# with open (r"data.txt","w") as f:
#     f.write(d)

# 读取数据函数
def readData():
    with open (r"data.txt","r") as f:
        # f.read得到json字符串（符合json格式）
        jsonData = f.read()
        # json.loads()得到python对象
        dataList = json.loads(jsonData)
        return dataList

def writeData(dataList):
    # 将python对象转化为json字符串
    jsonData = json.dumps(dataList,ensure_ascii=False)
    with open(f"data.txt","w") as f:
        f.write(jsonData)


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

 # 增加数据
def addData(content,amount,cla):
    dataList = readData()
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    data = {"时间":t,"项目":content,"金额":amount,"分类":cla}
    dataList.append(data)
    writeData(dataList)

# 删除数据
def deleteData(index):
    dataList = readData()
    if 0 <= index < len(dataList):
        dataList.pop(index)
        writeData(dataList)

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
    summary_label = tk.Label(window, text="总收入多少元，总支出多少元，结余多少元")
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
        summary_label.config(text=f"总收入{total_in}元，总支出{total_out}元，结余{balance}元")
        
  # 确认提交
    def submit():
        project = entry_project.get()
        amount = float(entry_amount.get())
        category = category_var.get()
        addData(project, amount, category)
        refresh_display()
        messagebox.showinfo('成功', '账单添加成功！')
    
    # 删除选中
    def delete_selected():
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

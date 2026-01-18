"""
学生信息管理系统主程序入口
"""
import tkinter as tk
from gui_interface import StudentManagementGUI


def main():
    """主函数"""
    # 创建主窗口
    root = tk.Tk()

    # 设置窗口图标和标题
    root.title("学生信息管理系统")

    # 创建GUI实例
    app = StudentManagementGUI(root)

    # 显示初始信息
    app.append_result("🎓 欢迎使用学生信息管理系统！")
    app.append_result("💡 使用指南：")
    app.append_result("  1. 点击上方按钮进行常规操作")
    app.append_result("  2. 在自然语言输入框中输入指令（如：添加学生张三）")
    app.append_result("  3. 支持上下文关联（如：先查询，再问'其中男生多少'）")
    app.append_result("\n📚 示例指令：")
    app.append_result("  • 添加学生李四，学号2023001，年龄18，男生，一班，电话13812345678")
    app.append_result("  • 把学号2023001的班级改成二班")
    app.append_result("  • 查询二班年龄在18-20岁之间的女生有多少人？")
    app.append_result("  • 统计各班级人数")

    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()

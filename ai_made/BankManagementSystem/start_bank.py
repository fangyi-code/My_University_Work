# start_bank.py - 统一的启动文件
import subprocess
import sys

def main():
    print("启动银行管理系统...")
    
    # 运行GUI登录界面
    try:
        # 导入GUI模块并运行
        from bank_gui import BankLoginGUI
        app = BankLoginGUI()
        app.run()
    except ImportError:
        print("GUI模块加载失败，使用命令行版本...")
        # 如果GUI模块不存在，直接运行命令行版本
        subprocess.run([sys.executable, "bank_main.py"])

if __name__ == "__main__":
    main()
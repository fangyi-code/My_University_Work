# GUI程序：图形用户界面
# 请先下载tkinter
import tkinter as tk
from tkinter import filedialog #上传图片需要用到filedialog模块

class ImageFormatError(Exception):
    # 魔法方法，当对象被转换为字符串时，显示内容
    def __str__(self):
        return "请使用BMP,PNG或JPEG格式的图片作为头像!"

class Image:
    def __init__(self):
        self.file_path = "1"

    def input_image(self):
        root = tk.Tk() #调用Tk类的构造函数，创建一个主窗口对象
        root.withdraw() #隐藏主窗口
        #file_path = filedialog.askopenfile(title = "请选择头像！") #askopenfile是filedialog模块中的函数，用于返回文件对象
        self.file_path = filedialog.askopenfilename(title = "请选择头像！") #返回文件路径字符串
        root.destroy() #关闭主窗口

        if not self.file_path:
            print("未选择文件")
            return False 
        return True

    def check(self):
        while True:
            try:
                png = self.file_path.lower().endswith('.png')
                bmp = self.file_path.lower().endswith('.bmp')
                jpeg = self.file_path.lower().endswith('.jpeg')
                # endswith:判断字符串是否以某个内容结尾
                if png or bmp or jpeg:
                    print("上传成功！")
                    break
                else:
                    raise ImageFormatError()

            except ImageFormatError as error:
                print(error)
                if not self.input_image():
                    print("取消选择,程序退出")
                    break
                continue

image = Image()
if image.input_image():
    image.check()
'''
1,如果用户输入的要备份的文件或目录不存在，则会创建该文件或目录后再进行备份操作；如果用户输入的要备份的文件或目录存在，则会直接进行备份操作。

2,如果用户输入的要备份的目录是一个文件夹，则遍历该文件夹下的所有文件并逐个备份。

3,如果用户输入的要备份的文件存在，则会直接对该文件进行备份操作，否则提示用户要备份的文件不存在，并退出程序。

4,备份操作是将源文件内容逐行复制到新文件中，保存在备份目录下，并以原文件名命名新文件。
'''
import os
import shutil

def sel():
    if os.path.exists(file):
        print(f"{file}存在！进行备份操作！")
        beifen()
    else:
        print(f"{file}不存在！是否创建该文件/目录？")
        choice = input("若要创建,请输入yes,否则将退出备份程序。")
        if choice == "yes":
            chuangjian()
        else:
            return False
    return True

def chuangjian():
    # endswith:python字符串方法，用于检查字符串是否以指定的后缀结尾。
    if file.endswith('/') or file.endswith('\\'):
        os.mkdir(file)
        print(f"已创建目录：{file}")
    else:
        with open(file,'w'):
            pass
        print(f"已创建文件：{file}")


def beifen():
    # 创建备份目录
    backup = "backup"
    # 避免目录存在报错
    # os.makedirs()可以创建多级目录，os.mkdir只能创建一级
    os.makedirs(backup,exist_ok=True)

    if os.path.isfile(file):
        beifen_file(backup)
    else:
        beifen_files(backup)

#备份文件
def beifen_file(backup):
    # 提取文件名
    filename = os.path.basename(file)
    # join进行组合
    target = os.path.join(backup,filename)
    with open(file,'r') as a,open(target,'w') as b:
        for i in a:
            b.write(i)
    print(f"已成功备份:{file},保存于{backup} 目录")

#备份目录
def beifen_files(backup):
    # restrip()去掉最右边的字符串
    files_path = file.rstrip('/\\')
    # os.listdir:获取文件名列表
    for filename in os.listdir(files_path):
        # 拼接文件路径
        source = os.path.join(files_path, filename)
        # 如果是文件..
        if os.path.isfile(source):
            # 拼接备份目录和文件
            target = os.path.join(backup, filename)
            # 复制！
            shutil.copy(source, target)
    print(f"已成功备份:{file},保存于{backup} 目录")


while True:
    file = input("请输入要备份的文件或目录：")
    result = sel()
    if result is False:
        print("退出程序！")
        break
        
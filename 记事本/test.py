# test_sg.py
print("步骤1: 开始...")
import sys
print(f"步骤2: Python版本 {sys.version}")

print("步骤3: 导入json...")
import json
print("步骤4: json导入成功")

print("步骤5: 准备导入PySimpleGUI...")
try:
    import PySimpleGUI as sg
    print("步骤6: PySimpleGUI导入成功")
    print(f"步骤7: PySimpleGUI版本 {sg.version}")
except Exception as e:
    print(f"步骤6: PySimpleGUI导入失败: {e}")
    import traceback
    traceback.print_exc()
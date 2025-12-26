from functools import reduce
# 要求1
students = [
{"name": "Alice", "math": 85, "physics": 92, "chemistry": 78},
{"name": "Bob", "math": 75, "physics": 88, "chemistry": 90},
{"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88}
]

def avg():
   for student in students:
       student["avg"] = (student['math']+student['physics']+student['chemistry']) /3
   a = list(map(lambda student:round(student.get("avg"),2), students))
   return a

result = avg()
print(f"平均分：{result}")

#要求2
# for student:从filter结果中逐个取出学生字典
a = [student["name"] for student in filter(lambda student:student["avg"] > 85, students)]
print(f"高分学生：{a}")

#要求3

result = sorted(students, key=lambda student: student["physics"], reverse=True)
print("按物理排序：")
for student in result:
    print(f"'name': {student['name']}",end = ',')
print()

#要求4
math_sum = reduce(lambda x, student: x + student["math"], students, 0)
print(f"所有学生数学成绩总和: {math_sum}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("任务2 测试：Lambda 与高阶函数")
    print("="*50)
# 测试学生数据处理
# 预期输出:
# 平均分: [{'name': 'Alice', 'avg': 85.0}, ...]
# 高分学生: [{'name': 'Alice', ...}, ...]
# 按物理排序: [{'name': 'Alice', ...}, ...]
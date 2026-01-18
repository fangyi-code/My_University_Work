"""
学生数据模型和文件操作模块
处理JSON数据的加载、保存和基本操作
"""
import json
import os
from typing import List, Dict, Any, Optional


class Student:
    """学生数据模型类"""

    def __init__(self, student_id: str, name: str, age: int,
                 gender: str, class_name: str, phone: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.class_name = class_name
        self.phone = phone

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "class_name": self.class_name,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        """从字典创建Student对象"""
        return cls(
            student_id=data.get("student_id", ""),
            name=data.get("name", ""),
            age=data.get("age", 0),
            gender=data.get("gender", ""),
            class_name=data.get("class_name", ""),
            phone=data.get("phone", "")
        )

    def __str__(self) -> str:
        return (f"学号: {self.student_id}, 姓名: {self.name}, "
                f"年龄: {self.age}, 性别: {self.gender}, "
                f"班级: {self.class_name}, 电话: {self.phone}")


class StudentManager:
    """学生数据管理类"""

    def __init__(self, filename: str = "students.json"):
        self.filename = filename
        self.students: List[Student] = []
        self.load_data()

    def load_data(self) -> None:
        """从JSON文件加载数据"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = [Student.from_dict(item) for item in data]
            else:
                self.students = []
                self.save_data()
        except Exception as e:
            print(f"加载数据失败: {e}")
            self.students = []

    def save_data(self) -> None:
        """保存数据到JSON文件"""
        try:
            data = [student.to_dict() for student in self.students]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据失败: {e}")

    def add_student(self, student: Student) -> bool:
        """添加学生，检查学号唯一性"""
        if any(s.student_id == student.student_id for s in self.students):
            return False
        self.students.append(student)
        self.save_data()
        return True

    def delete_student(self, student_id: str) -> bool:
        """按学号删除学生"""
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < initial_count:
            self.save_data()
            return True
        return False

    def update_student(self, student_id: str, **kwargs) -> bool:
        """按学号更新学生信息"""
        for student in self.students:
            if student.student_id == student_id:
                for key, value in kwargs.items():
                    if hasattr(student, key):
                        setattr(student, key, value)
                self.save_data()
                return True
        return False

    def get_student(self, student_id: str) -> Optional[Student]:
        """按学号获取学生"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_by_class(self, class_name: str) -> List[Student]:
        """按班级查询学生"""
        return [s for s in self.students if s.class_name == class_name]

    def search_by_age_range(self, min_age: int, max_age: int) -> List[Student]:
        """按年龄范围查询学生"""
        return [s for s in self.students if min_age <= s.age <= max_age]

    def search_by_gender(self, gender: str) -> List[Student]:
        """按性别查询学生"""
        return [s for s in self.students if s.gender == gender]

    def get_all_students(self) -> List[Student]:
        """获取所有学生"""
        return self.students.copy()

    def get_students_by_conditions(self, **conditions) -> List[Student]:
        """多条件查询学生"""
        result = self.students

        if 'class_name' in conditions:
            result = [s for s in result if s.class_name == conditions['class_name']]
        if 'gender' in conditions:
            result = [s for s in result if s.gender == conditions['gender']]
        if 'min_age' in conditions and 'max_age' in conditions:
            result = [s for s in result if conditions['min_age'] <= s.age <= conditions['max_age']]

        return result
"""
智能校验模块
验证输入数据的合法性和合理性
"""
import re
from typing import Tuple, Optional


class Validator:
    """数据验证器"""

    # 定义校验规则
    AGE_RANGE = (10, 22)  # 年龄范围
    PHONE_PATTERN = r'^1[3-9]\d{9}$'  # 手机号正则
    CLASS_PATTERNS = [r'^\d+班$', r'^[一二三四五六七八九十]+班$']  # 班级格式

    @staticmethod
    def validate_age(age_str: str) -> Tuple[bool, Optional[str]]:
        """验证年龄"""
        try:
            age = int(age_str)
            if age < Validator.AGE_RANGE[0] or age > Validator.AGE_RANGE[1]:
                return False, f"年龄超出合理范围({Validator.AGE_RANGE[0]}-{Validator.AGE_RANGE[1]})"
            return True, None
        except ValueError:
            return False, "年龄必须是数字"

    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, Optional[str]]:
        """验证电话号码格式"""
        if re.match(Validator.PHONE_PATTERN, phone):
            return True, None
        return False, "电话格式错误(应为11位数字，以1开头)"

    @staticmethod
    def validate_class_name(class_name: str) -> Tuple[bool, Optional[str]]:
        """验证班级格式"""
        for pattern in Validator.CLASS_PATTERNS:
            if re.match(pattern, class_name):
                return True, None
        return False, "班级格式错误(应为'一班'或'1班'格式)"

    @staticmethod
    def validate_student_id(student_id: str, existing_ids: list) -> Tuple[bool, Optional[str]]:
        """验证学号唯一性"""
        if not student_id:
            return False, "学号不能为空"
        if student_id in existing_ids:
            return False, "学号已存在"
        return True, None

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, Optional[str]]:
        """验证姓名"""
        if not name or not name.strip():
            return False, "姓名不能为空"
        if len(name) > 20:
            return False, "姓名过长(不超过20字符)"
        return True, None

    @staticmethod
    def validate_gender(gender: str) -> Tuple[bool, Optional[str]]:
        """验证性别"""
        if gender in ['男', '女', '男生', '女生']:
            return True, None
        return False, "性别应为'男'或'女'"

    @staticmethod
    def validate_all(student_data: dict, existing_ids: list = None) -> Tuple[bool, Optional[str]]:
        """综合验证所有字段"""
        if existing_ids is None:
            existing_ids = []

        # 验证学号
        if 'student_id' in student_data:
            valid, msg = Validator.validate_student_id(
                student_data['student_id'], existing_ids
            )
            if not valid:
                return False, msg

        # 验证姓名
        if 'name' in student_data:
            valid, msg = Validator.validate_name(student_data['name'])
            if not valid:
                return False, msg

        # 验证年龄
        if 'age' in student_data:
            if isinstance(student_data['age'], str):
                valid, msg = Validator.validate_age(student_data['age'])
            else:
                valid, msg = Validator.validate_age(str(student_data['age']))
            if not valid:
                return False, msg

        # 验证性别
        if 'gender' in student_data:
            valid, msg = Validator.validate_gender(student_data['gender'])
            if not valid:
                return False, msg

        # 验证班级
        if 'class_name' in student_data:
            valid, msg = Validator.validate_class_name(student_data['class_name'])
            if not valid:
                return False, msg

        # 验证电话
        if 'phone' in student_data:
            valid, msg = Validator.validate_phone(student_data['phone'])
            if not valid:
                return False, msg

        return True, None
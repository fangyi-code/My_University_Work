
"""
自然语言处理模块
解析用户输入的自然语言指令
"""
import re
from typing import Tuple, Dict, Any, Optional, List
from student_model import Student


class NaturalLanguageProcessor:
    """自然语言处理器"""

    # 操作关键词映射
    OPERATION_KEYWORDS = {
        'add': ['添加', '增加', '新建', '创建', '新增'],
        'delete': ['删除', '移除', '删掉', '去掉'],
        'update': ['修改', '更新', '改变', '更改', '改成'],
        'query': ['查询', '查找', '搜索', '查看', '找出', '显示'],
        'statistics': ['统计', '数量', '人数', '多少', '占比']
    }

    # 字段关键词映射
    FIELD_KEYWORDS = {
        'student_id': ['学号', '编号', 'id'],
        'name': ['姓名', '名字', '名称'],
        'age': ['年龄', '岁数', '年纪'],
        'gender': ['性别', '男', '女'],
        'class_name': ['班级', '班'],
        'phone': ['电话', '手机', '联系方式', '手机号']
    }

    @staticmethod
    def parse_intent(text: str) -> Tuple[str, Dict[str, Any]]:
        """解析用户意图和参数"""
        text = text.strip()

        # 检测操作类型
        operation = None
        for op, keywords in NaturalLanguageProcessor.OPERATION_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                operation = op
                break

        if not operation:
            return "unknown", {"text": text}

        # 解析不同操作的参数
        if operation == 'add':
            return operation, NaturalLanguageProcessor._parse_add(text)
        elif operation == 'update':
            return operation, NaturalLanguageProcessor._parse_update(text)
        elif operation == 'delete':
            return operation, NaturalLanguageProcessor._parse_delete(text)
        elif operation == 'query':
            return operation, NaturalLanguageProcessor._parse_query(text)
        elif operation == 'statistics':
            return operation, NaturalLanguageProcessor._parse_statistics(text)

        return "unknown", {"text": text}

    @staticmethod
    def _parse_add(text: str) -> Dict[str, Any]:
        """解析添加操作的参数"""
        params = {}

        # 提取学号
        id_match = re.search(r'学号\s*(\d+)', text)
        if id_match:
            params['student_id'] = id_match.group(1)

        # 提取姓名
        name_match = re.search(r'姓?名?[：:]?\s*([\u4e00-\u9fa5]{2,4})', text)
        if name_match:
            params['name'] = name_match.group(1)

        # 提取年龄
        age_match = re.search(r'年龄?\s*(\d+)', text)
        if age_match:
            params['age'] = int(age_match.group(1))

        # 提取性别
        if '男' in text or '男生' in text:
            params['gender'] = '男'
        elif '女' in text or '女生' in text:
            params['gender'] = '女'

        # 提取班级 - 修复正则表达式
        class_match = re.search(r'([一二三四五六七八九十\d]+班)', text)
        if class_match:
            params['class_name'] = class_match.group(1)

        # 提取电话
        phone_match = re.search(r'1[3-9]\d{9}', text)
        if phone_match:
            params['phone'] = phone_match.group(0)

        return params

    @staticmethod
    def _parse_update(text: str) -> Dict[str, Any]:
        """解析修改操作的参数"""
        params = {}

        # 提取学号
        id_match = re.search(r'学号\s*(\d+)', text)
        if id_match:
            params['student_id'] = id_match.group(1)

        # 提取要修改的字段和值
        if '班级' in text:
            class_match = re.search(r'改成?\s*([一二三四五六七八九十\d]+班)', text)
            if class_match:
                params['class_name'] = class_match.group(1)

        if '电话' in text or '手机' in text:
            phone_match = re.search(r'1[3-9]\d{9}', text)
            if phone_match:
                params['phone'] = phone_match.group(0)

        if '年龄' in text:
            age_match = re.search(r'年龄?\s*(\d+)', text)
            if age_match:
                params['age'] = int(age_match.group(1))

        return params

    @staticmethod
    def _parse_delete(text: str) -> Dict[str, Any]:
        """解析删除操作的参数"""
        params = {}

        # 提取学号
        id_match = re.search(r'学号\s*(\d+)', text)
        if id_match:
            params['student_id'] = id_match.group(1)

        return params

    @staticmethod
    def _parse_query(text: str) -> Dict[str, Any]:
        """解析查询操作的参数"""
        params = {}

        # 精确查询学号
        id_match = re.search(r'学号\s*(\d+)', text)
        if id_match:
            params['student_id'] = id_match.group(1)
            params['query_type'] = 'exact'
            return params

        # 班级查询 - 修复正则表达式
        class_match = re.search(r'([一二三四五六七八九十\d]+班)', text)
        if class_match:
            params['class_name'] = class_match.group(1)

        # 年龄范围查询
        age_range_match = re.search(r'(\d+)[-到至](\d+)岁?', text)
        if age_range_match:
            params['min_age'] = int(age_range_match.group(1))
            params['max_age'] = int(age_range_match.group(2))

        # 性别查询
        if '男生' in text or '男' in text:
            params['gender'] = '男'
        elif '女生' in text or '女' in text:
            params['gender'] = '女'

        params['query_type'] = 'condition'
        return params

    @staticmethod
    def _parse_statistics(text: str) -> Dict[str, Any]:
        """解析统计操作的参数"""
        params = {}

        # 班级人数统计
        if '班级' in text and '人数' in text:
            params['stat_type'] = 'class_count'

        # 年龄性别统计
        if '多少' in text or '数量' in text:
            params['stat_type'] = 'count'

            # 提取班级 - 修复正则表达式
            class_match = re.search(r'([一二三四五六七八九十\d]+班)', text)
            if class_match:
                params['class_name'] = class_match.group(1)

            # 提取年龄范围
            age_range_match = re.search(r'(\d+)[-到至](\d+)岁?', text)
            if age_range_match:
                params['min_age'] = int(age_range_match.group(1))
                params['max_age'] = int(age_range_match.group(2))

            # 提取性别
            if '男生' in text or '男' in text:
                params['gender'] = '男'
            elif '女生' in text or '女' in text:
                params['gender'] = '女'

        return params

    @staticmethod
    def format_response(operation: str, result: Any, params: Dict = None) -> str:
        """格式化响应文本"""
        if operation == 'add':
            if result:
                return f"[成功] 添加学生：{params.get('name', '')} (学号: {params.get('student_id', '')})"
            else:
                return f"[失败] 添加失败：学号 {params.get('student_id', '')} 已存在"

        elif operation == 'update':
            if result:
                return f"[成功] 更新学号 {params.get('student_id', '')} 的学生信息"
            else:
                return f"[失败] 更新失败：未找到学号 {params.get('student_id', '')} 的学生"

        elif operation == 'delete':
            if result:
                return f"[成功] 删除学号 {params.get('student_id', '')} 的学生"
            else:
                return f"[失败] 删除失败：未找到学号 {params.get('student_id', '')} 的学生"

        elif operation == 'query':
            if isinstance(result, list):
                if len(result) == 0:
                    return "[查询] 未找到符合条件的学生"
                else:
                    students_info = "\n".join([f"  • {str(s)}" for s in result])
                    return f"[查询] 找到 {len(result)} 名学生：\n{students_info}"
            elif result:
                return f"[查询] 查询结果：\n  • {str(result)}"
            else:
                return "[查询] 未找到该学生"

        elif operation == 'statistics':
            return result if isinstance(result, str) else str(result)

        return "[帮助] 无法识别您的指令"

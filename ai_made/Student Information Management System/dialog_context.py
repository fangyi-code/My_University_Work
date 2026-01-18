"""
对话上下文管理模块
支持多轮对话的记忆
"""
from typing import List, Optional
from collections import deque


class DialogContext:
    """对话上下文管理器"""

    def __init__(self, max_history: int = 3):
        self.max_history = max_history
        self.history = deque(maxlen=max_history)
        self.last_query_result = None  # 上次查询结果

    def add_to_history(self, user_input: str, system_response: str, result_data=None):
        """添加对话到历史"""
        self.history.append({
            'user': user_input,
            'system': system_response
        })
        if result_data is not None:
            self.last_query_result = result_data

    def get_history(self) -> List[dict]:
        """获取对话历史"""
        return list(self.history)

    def clear_history(self):
        """清空对话历史"""
        self.history.clear()
        self.last_query_result = None

    def process_with_context(self, current_input: str) -> str:
        """结合上下文处理当前输入"""
        if not self.history:
            return current_input

        # 处理上下文关联词
        context_keywords = ['其中', '这些', '他们', '上面', '前面', '刚才']

        for keyword in context_keywords:
            if keyword in current_input:
                # 尝试从上次查询结果中提取信息
                if self.last_query_result:
                    # 如果是查询特定群体中的统计
                    if '多少' in current_input or '数量' in current_input:
                        # 从current_input提取条件
                        conditions = self._extract_conditions(current_input)
                        # 在上次结果中筛选
                        return self._filter_last_result(conditions)
                break

        return current_input

    def _extract_conditions(self, text: str) -> dict:
        """从文本中提取条件"""
        conditions = {}

        if '男生' in text or '男' in text:
            conditions['gender'] = '男'
        elif '女生' in text or '女' in text:
            conditions['gender'] = '女'

        # 提取年龄范围
        import re
        age_match = re.search(r'(\d+)[-到至](\d+)岁?', text)
        if age_match:
            conditions['min_age'] = int(age_match.group(1))
            conditions['max_age'] = int(age_match.group(2))

        return conditions

    def _filter_last_result(self, conditions: dict) -> str:
        """在上次结果中筛选"""
        if not self.last_query_result or not isinstance(self.last_query_result, list):
            return "无法找到相关的上下文信息"

        from student_model import Student
        filtered = self.last_query_result

        if 'gender' in conditions:
            filtered = [s for s in filtered if isinstance(s, Student) and s.gender == conditions['gender']]

        if 'min_age' in conditions and 'max_age' in conditions:
            filtered = [s for s in filtered if isinstance(s, Student) and
                        conditions['min_age'] <= s.age <= conditions['max_age']]

        return f"在上一组结果中，满足条件的有 {len(filtered)} 人"
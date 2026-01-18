"""
统计分析和机器学习模块
生成统计报告和预测模型
"""
from typing import List, Dict, Any, Tuple
import math
from collections import Counter
from student_model import Student


class StatisticsAnalyzer:
    """统计分析器"""

    @staticmethod
    def generate_report(students: List[Student]) -> str:
        """生成统计报告"""
        if not students:
            return "当前没有学生数据"

        total = len(students)
        report_lines = [f"📊 学生信息统计报告", f"总计学生人数: {total}人"]

        # 按班级统计
        class_counts = Counter(s.class_name for s in students)
        report_lines.append("\n📈 各班级人数:")
        for class_name, count in class_counts.items():
            percentage = (count / total) * 100
            report_lines.append(f"  {class_name}: {count}人 ({percentage:.1f}%)")

        # 按性别统计
        gender_counts = Counter(s.gender for s in students)
        report_lines.append("\n🚻 性别分布:")
        for gender, count in gender_counts.items():
            percentage = (count / total) * 100
            report_lines.append(f"  {gender}: {count}人 ({percentage:.1f}%)")

        # 年龄统计
        if students:
            ages = [s.age for s in students]
            avg_age = sum(ages) / len(ages)
            min_age = min(ages)
            max_age = max(ages)
            report_lines.append(f"\n🎂 年龄统计:")
            report_lines.append(f"  平均年龄: {avg_age:.1f}岁")
            report_lines.append(f"  最小年龄: {min_age}岁")
            report_lines.append(f"  最大年龄: {max_age}岁")

        # 人数最多的班级
        if class_counts:
            most_common_class, most_count = class_counts.most_common(1)[0]
            report_lines.append(f"\n🏆 人数最多的班级: {most_common_class} ({most_count}人)")

        return "\n".join(report_lines)

    @staticmethod
    def count_by_conditions(students: List[Student], **conditions) -> str:
        """按条件统计人数"""
        filtered = students

        if 'class_name' in conditions:
            filtered = [s for s in filtered if s.class_name == conditions['class_name']]

        if 'gender' in conditions:
            filtered = [s for s in filtered if s.gender == conditions['gender']]

        if 'min_age' in conditions and 'max_age' in conditions:
            filtered = [s for s in filtered if
                        conditions['min_age'] <= s.age <= conditions['max_age']]

        # 构建条件描述
        conditions_desc = []
        if 'class_name' in conditions:
            conditions_desc.append(f"班级: {conditions['class_name']}")
        if 'gender' in conditions:
            conditions_desc.append(f"性别: {conditions['gender']}")
        if 'min_age' in conditions and 'max_age' in conditions:
            conditions_desc.append(f"年龄: {conditions['min_age']}-{conditions['max_age']}岁")

        desc = "，".join(conditions_desc)
        return f"符合条件「{desc}」的学生有 {len(filtered)} 人"


class NaiveBayesPredictor:
    """朴素贝叶斯预测器"""

    def __init__(self):
        self.class_probs = {}  # 班级先验概率
        self.feature_probs = {}  # 特征条件概率
        self.is_trained = False

    def train(self, students: List[Student]) -> None:
        """训练朴素贝叶斯模型"""
        if not students:
            return

        # 计算班级先验概率
        total = len(students)
        class_counts = Counter(s.class_name for s in students)
        self.class_probs = {cls: count / total for cls, count in class_counts.items()}

        # 计算特征条件概率
        self.feature_probs = {}

        for class_name in self.class_probs.keys():
            class_students = [s for s in students if s.class_name == class_name]
            class_count = len(class_students)

            # 年龄分布（简化处理：按年龄段）
            age_groups = {}
            ages = [s.age for s in class_students]
            if ages:
                age_mean = sum(ages) / len(ages)
                age_std = math.sqrt(sum((x - age_mean) ** 2 for x in ages) / len(ages))
                age_groups = {
                    'mean': age_mean,
                    'std': age_std
                }

            # 性别分布
            gender_counts = Counter(s.gender for s in class_students)
            gender_probs = {gender: (count + 1) / (class_count + 2)  # 拉普拉斯平滑
                            for gender, count in gender_counts.items()}

            self.feature_probs[class_name] = {
                'age': age_groups,
                'gender': gender_probs
            }

        self.is_trained = True

    def predict(self, age: int, gender: str) -> Tuple[str, float]:
        """预测学生班级"""
        if not self.is_trained:
            return "未训练模型", 0.0

        if not self.feature_probs:
            return "无数据可预测", 0.0

        best_class = None
        best_prob = -1.0

        for class_name, class_prob in self.class_probs.items():
            feature_prob = self.feature_probs[class_name]

            # 计算年龄概率（基于正态分布假设）
            age_prob = 1.0
            if feature_prob['age']:
                mean = feature_prob['age']['mean']
                std = feature_prob['age']['std'] + 1e-6  # 避免除零
                # 简化：使用高斯分布概率密度
                age_prob = math.exp(-0.5 * ((age - mean) / std) ** 2) / (std * math.sqrt(2 * math.pi))

            # 计算性别概率
            gender_prob = feature_prob['gender'].get(gender, 0.01)  # 平滑处理

            # 后验概率 = 先验概率 * 年龄概率 * 性别概率
            posterior = class_prob * age_prob * gender_prob

            if posterior > best_prob:
                best_prob = posterior
                best_class = class_name

        return best_class, best_prob

    def predict_from_dict(self, student_data: dict) -> Tuple[str, float]:
        """从字典数据预测"""
        age = student_data.get('age', 18)
        gender = student_data.get('gender', '男')

        # 标准化性别输入
        if gender in ['男生', '男']:
            gender = '男'
        elif gender in ['女生', '女']:
            gender = '女'

        return self.predict(age, gender)
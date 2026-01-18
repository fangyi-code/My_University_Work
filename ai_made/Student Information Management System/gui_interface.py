"""
图形用户界面模块
基于tkinter的GUI实现
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import Optional, Callable
from student_model import Student, StudentManager
from validator import Validator
from natural_language import NaturalLanguageProcessor
from dialog_context import DialogContext
from statistics import StatisticsAnalyzer, NaiveBayesPredictor


class StudentManagementGUI:
    """学生信息管理GUI"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("学生信息管理系统")
        self.root.geometry("1000x700")

        # 初始化组件
        self.student_manager = StudentManager()
        self.validator = Validator()
        self.nlp = NaturalLanguageProcessor()
        self.dialog_context = DialogContext()
        self.statistics_analyzer = StatisticsAnalyzer()
        self.predictor = NaiveBayesPredictor()

        # 训练预测模型
        self.predictor.train(self.student_manager.get_all_students())

        # 当前操作模式
        self.current_mode = "menu"

        # 创建界面
        self.setup_ui()

        # 绑定关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self) -> None:
        """设置用户界面"""
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="🎓 学生信息管理系统",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # 自然语言输入区域
        ttk.Label(main_frame, text="💬 自然语言输入:").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))

        self.natural_language_entry = ttk.Entry(main_frame, width=60)
        self.natural_language_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 5), padx=(5, 0))

        natural_language_btn = ttk.Button(
            main_frame,
            text="执行",
            command=self.process_natural_language
        )
        natural_language_btn.grid(row=1, column=2, padx=(5, 0), pady=(0, 5))

        # 操作按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        operations = [
            ("➕ 添加学生", self.show_add_form),
            ("✏️ 修改学生", self.show_update_form),
            ("🗑️ 删除学生", self.show_delete_form),
            ("🔍 查询学生", self.show_query_form),
            ("📊 统计报告", self.show_statistics),
            ("📋 显示所有", self.show_all_students),
            ("🤖 预测班级", self.show_predict_form),
            ("🔄 重置界面", self.reset_interface)
        ]

        for i, (text, command) in enumerate(operations):
            btn = ttk.Button(button_frame, text=text, command=command)
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

        # 结果显示区域
        result_label = ttk.Label(main_frame, text="📋 结果输出:")
        result_label.grid(row=3, column=0, sticky=tk.W, pady=(10, 5))

        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            width=80,
            height=20,
            wrap=tk.WORD,
            font=("Consolas", 10)
        )
        self.result_text.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        # 状态栏
        self.status_var = tk.StringVar(value="就绪")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN
        )
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 0))

    def show_add_form(self) -> None:
        """显示添加学生表单"""
        self.clear_result()
        self.current_mode = "add"

        form_window = tk.Toplevel(self.root)
        form_window.title("添加学生")
        form_window.geometry("400x400")

        # 表单字段
        fields = [
            ("学号:", "student_id"),
            ("姓名:", "name"),
            ("年龄:", "age"),
            ("性别:", "gender"),
            ("班级:", "class_name"),
            ("电话:", "phone")
        ]

        entries = {}

        for i, (label, key) in enumerate(fields):
            ttk.Label(form_window, text=label).grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

            if key == 'gender':
                gender_var = tk.StringVar()
                gender_combobox = ttk.Combobox(
                    form_window,
                    textvariable=gender_var,
                    values=["男", "女"],
                    width=20
                )
                gender_combobox.grid(row=i, column=1, padx=10, pady=10)
                entries[key] = gender_var
            else:
                entry = ttk.Entry(form_window, width=25)
                entry.grid(row=i, column=1, padx=10, pady=10)
                entries[key] = entry

        # 添加按钮
        button_frame = ttk.Frame(form_window)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        ttk.Button(
            button_frame,
            text="添加",
            command=lambda: self.add_student_from_form(entries, form_window)
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="取消",
            command=form_window.destroy
        ).pack(side=tk.LEFT, padx=5)

    def add_student_from_form(self, entries: dict, window: tk.Toplevel) -> None:
        """从表单添加学生"""
        try:
            # 收集数据
            student_data = {}

            for key, entry in entries.items():
                if isinstance(entry, tk.StringVar):
                    value = entry.get()
                else:
                    value = entry.get()

                if key == 'age' and value:
                    value = int(value)

                student_data[key] = value

            # 验证数据
            existing_ids = [s.student_id for s in self.student_manager.get_all_students()]
            valid, message = Validator.validate_all(student_data, existing_ids)

            if not valid:
                messagebox.showerror("验证错误", message)
                return

            # 创建学生对象
            student = Student(
                student_id=student_data['student_id'],
                name=student_data['name'],
                age=student_data['age'],
                gender=student_data['gender'],
                class_name=student_data['class_name'],
                phone=student_data['phone']
            )

            # 添加学生
            success = self.student_manager.add_student(student)

            if success:
                self.append_result(f"✅ 成功添加学生：{student.name} (学号: {student.student_id})")
                self.status_var.set(f"添加学生成功 - {student.name}")
                window.destroy()

                # 重新训练预测模型
                self.predictor.train(self.student_manager.get_all_students())
            else:
                messagebox.showerror("添加失败", f"学号 {student.student_id} 已存在")

        except ValueError as e:
            messagebox.showerror("输入错误", f"请输入正确的数据格式：{e}")
        except Exception as e:
            messagebox.showerror("错误", f"添加失败：{e}")

    def show_update_form(self) -> None:
        """显示修改学生表单"""
        self.clear_result()
        self.current_mode = "update"

        form_window = tk.Toplevel(self.root)
        form_window.title("修改学生信息")
        form_window.geometry("500x300")

        # 学号输入
        ttk.Label(form_window, text="学号:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        student_id_entry = ttk.Entry(form_window, width=25)
        student_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # 查询按钮
        def find_student():
            student_id = student_id_entry.get()
            student = self.student_manager.get_student(student_id)

            if student:
                self.show_update_fields(form_window, student)
            else:
                messagebox.showwarning("未找到", f"未找到学号为 {student_id} 的学生")

        ttk.Button(
            form_window,
            text="查询",
            command=find_student
        ).grid(row=0, column=2, padx=10, pady=10)

    def show_update_fields(self, window: tk.Toplevel, student: Student) -> None:
        """显示更新字段表单"""
        # 清除旧内容
        for widget in window.winfo_children():
            if widget.winfo_y() > 40:
                widget.destroy()

        # 创建更新字段
        fields_frame = ttk.Frame(window)
        fields_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # 显示当前信息
        current_info = f"当前信息: {student.name}, {student.age}岁, {student.class_name}"
        ttk.Label(fields_frame, text=current_info).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # 更新字段
        update_fields = [
            ("新班级:", "class_name", student.class_name),
            ("新电话:", "phone", student.phone),
            ("新年龄:", "age", str(student.age)),
            ("新性别:", "gender", student.gender)
        ]

        entries = {}

        for i, (label, key, default) in enumerate(update_fields):
            ttk.Label(fields_frame, text=label).grid(row=i + 1, column=0, padx=5, pady=5, sticky=tk.W)

            if key == 'gender':
                gender_var = tk.StringVar(value=default)
                gender_combobox = ttk.Combobox(
                    fields_frame,
                    textvariable=gender_var,
                    values=["男", "女"],
                    width=20
                )
                gender_combobox.grid(row=i + 1, column=1, padx=5, pady=5)
                entries[key] = gender_var
            else:
                entry = ttk.Entry(fields_frame, width=25)
                entry.insert(0, default)
                entry.grid(row=i + 1, column=1, padx=5, pady=5)
                entries[key] = entry

        # 更新按钮
        def update_student():
            try:
                update_data = {}

                for key, entry in entries.items():
                    if isinstance(entry, tk.StringVar):
                        value = entry.get()
                    else:
                        value = entry.get()

                    if key == 'age' and value:
                        value = int(value)

                    if value != getattr(student, key):
                        update_data[key] = value

                if update_data:
                    # 验证数据
                    valid, message = Validator.validate_all(update_data)

                    if not valid:
                        messagebox.showerror("验证错误", message)
                        return

                    # 更新学生
                    success = self.student_manager.update_student(student.student_id, **update_data)

                    if success:
                        self.append_result(f"✅ 成功更新学生 {student.name} 的信息")
                        self.status_var.set(f"更新成功 - {student.name}")
                        window.destroy()

                        # 重新训练预测模型
                        self.predictor.train(self.student_manager.get_all_students())
                    else:
                        messagebox.showerror("更新失败", "更新失败")
                else:
                    messagebox.showinfo("无变化", "未修改任何字段")

            except ValueError as e:
                messagebox.showerror("输入错误", f"请输入正确的数据格式：{e}")
            except Exception as e:
                messagebox.showerror("错误", f"更新失败：{e}")

        ttk.Button(
            fields_frame,
            text="更新",
            command=update_student
        ).grid(row=len(update_fields) + 1, column=0, columnspan=2, pady=20)

    def show_delete_form(self) -> None:
        """显示删除学生表单"""
        self.clear_result()
        self.current_mode = "delete"

        form_window = tk.Toplevel(self.root)
        form_window.title("删除学生")
        form_window.geometry("300x150")

        # 学号输入
        ttk.Label(form_window, text="学号:").grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)
        student_id_entry = ttk.Entry(form_window, width=20)
        student_id_entry.grid(row=0, column=1, padx=10, pady=20)

        # 删除按钮
        def delete_student():
            student_id = student_id_entry.get()

            if not student_id:
                messagebox.showwarning("输入错误", "请输入学号")
                return

            # 确认对话框
            student = self.student_manager.get_student(student_id)
            if not student:
                messagebox.showwarning("未找到", f"未找到学号为 {student_id} 的学生")
                return

            confirm = messagebox.askyesno(
                "确认删除",
                f"确定要删除学生 {student.name} (学号: {student_id}) 吗？"
            )

            if confirm:
                success = self.student_manager.delete_student(student_id)

                if success:
                    self.append_result(f"✅成功删除学生 {student.name}")
                    self.status_var.set(f"删除成功 - {student.name}")
                    form_window.destroy()

                    # 重新训练预测模型
                    self.predictor.train(self.student_manager.get_all_students())
                else:
                    messagebox.showerror("删除失败", "删除失败")

        button_frame = ttk.Frame(form_window)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Button(
            button_frame,
            text="删除",
            command=delete_student
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="取消",
            command=form_window.destroy
        ).pack(side=tk.LEFT, padx=5)

    def show_query_form(self) -> None:
        """显示查询学生表单"""
        self.clear_result()
        self.current_mode = "query"

        form_window = tk.Toplevel(self.root)
        form_window.title("查询学生")
        form_window.geometry("400x300")

        # 查询类型选择
        query_type = tk.StringVar(value="exact")

        ttk.Radiobutton(
            form_window,
            text="按学号精确查询",
            variable=query_type,
            value="exact"
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

        ttk.Radiobutton(
            form_window,
            text="按条件查询",
            variable=query_type,
            value="condition"
        ).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

        # 精确查询字段
        exact_frame = ttk.LabelFrame(form_window, text="精确查询")
        exact_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(exact_frame, text="学号:").grid(row=0, column=0, padx=5, pady=5)
        exact_id_entry = ttk.Entry(exact_frame, width=20)
        exact_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # 条件查询字段
        condition_frame = ttk.LabelFrame(form_window, text="条件查询")
        condition_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(condition_frame, text="班级:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        class_entry = ttk.Entry(condition_frame, width=15)
        class_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(condition_frame, text="年龄范围:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        age_frame = ttk.Frame(condition_frame)
        age_frame.grid(row=1, column=1, padx=5, pady=5)

        min_age_entry = ttk.Entry(age_frame, width=5)
        min_age_entry.grid(row=0, column=0)
        ttk.Label(age_frame, text="-").grid(row=0, column=1, padx=2)
        max_age_entry = ttk.Entry(age_frame, width=5)
        max_age_entry.grid(row=0, column=2)

        ttk.Label(condition_frame, text="性别:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        gender_var = tk.StringVar()
        gender_combobox = ttk.Combobox(
            condition_frame,
            textvariable=gender_var,
            values=["", "男", "女"],
            width=10
        )
        gender_combobox.grid(row=2, column=1, padx=5, pady=5)

        # 查询按钮
        def perform_query():
            if query_type.get() == "exact":
                student_id = exact_id_entry.get()
                if student_id:
                    student = self.student_manager.get_student(student_id)
                    if student:
                        self.append_result(f"🔍 查询结果：\n  • {str(student)}")
                    else:
                        self.append_result("🔍 未找到该学生")
                else:
                    messagebox.showwarning("输入错误", "请输入学号")

            else:  # 条件查询
                conditions = {}

                class_name = class_entry.get()
                if class_name:
                    conditions['class_name'] = class_name

                min_age = min_age_entry.get()
                max_age = max_age_entry.get()
                if min_age and max_age:
                    try:
                        conditions['min_age'] = int(min_age)
                        conditions['max_age'] = int(max_age)
                    except ValueError:
                        messagebox.showerror("输入错误", "年龄必须是数字")
                        return

                gender = gender_var.get()
                if gender:
                    conditions['gender'] = gender

                if conditions:
                    students = self.student_manager.get_students_by_conditions(**conditions)

                    if students:
                        students_info = "\n".join([f"  • {str(s)}" for s in students])
                        self.append_result(f"🔍 找到 {len(students)} 名学生：\n{students_info}")
                    else:
                        self.append_result("🔍 未找到符合条件的学生")
                else:
                    messagebox.showwarning("输入错误", "请至少输入一个查询条件")

            form_window.destroy()

        ttk.Button(
            form_window,
            text="查询",
            command=perform_query
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def show_statistics(self) -> None:
        """显示统计报告"""
        self.clear_result()
        self.current_mode = "statistics"

        students = self.student_manager.get_all_students()
        report = StatisticsAnalyzer.generate_report(students)
        self.append_result(report)
        self.status_var.set("已生成统计报告")

    def show_all_students(self) -> None:
        """显示所有学生"""
        self.clear_result()
        self.current_mode = "all"

        students = self.student_manager.get_all_students()

        if not students:
            self.append_result("当前没有学生数据")
        else:
            self.append_result(f"📋 所有学生信息 (共 {len(students)} 人):")
            for i, student in enumerate(students, 1):
                self.append_result(f"\n{i}. {str(student)}")

        self.status_var.set(f"显示所有学生 - 共 {len(students)} 人")

    def show_predict_form(self) -> None:
        """显示班级预测表单"""
        self.clear_result()
        self.current_mode = "predict"

        form_window = tk.Toplevel(self.root)
        form_window.title("预测学生班级")
        form_window.geometry("300x200")

        # 输入字段
        fields = [
            ("年龄:", "age"),
            ("性别:", "gender")
        ]

        entries = {}

        for i, (label, key) in enumerate(fields):
            ttk.Label(form_window, text=label).grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

            if key == 'gender':
                gender_var = tk.StringVar()
                gender_combobox = ttk.Combobox(
                    form_window,
                    textvariable=gender_var,
                    values=["男", "女"],
                    width=15
                )
                gender_combobox.grid(row=i, column=1, padx=10, pady=10)
                entries[key] = gender_var
            else:
                entry = ttk.Entry(form_window, width=15)
                entry.grid(row=i, column=1, padx=10, pady=10)
                entries[key] = entry

        # 预测按钮
        def predict_class():
            try:
                age = int(entries['age'].get())
                gender = entries['gender'].get()

                if gender in ['男生', '男']:
                    gender = '男'
                elif gender in ['女生', '女']:
                    gender = '女'

                predicted_class, probability = self.predictor.predict(age, gender)

                if predicted_class != "未训练模型" and predicted_class != "无数据可预测":
                    self.append_result(
                        f"🤖 预测结果：\n"
                        f"  年龄: {age}岁\n"
                        f"  性别: {gender}\n"
                        f"  预测班级: {predicted_class}\n"
                        f"  置信度: {probability:.2%}"
                    )
                    self.status_var.set(f"预测完成 - 建议班级: {predicted_class}")
                else:
                    messagebox.showinfo("预测结果", predicted_class)

                form_window.destroy()

            except ValueError:
                messagebox.showerror("输入错误", "请输入正确的年龄（数字）")
            except Exception as e:
                messagebox.showerror("错误", f"预测失败：{e}")

        ttk.Button(
            form_window,
            text="预测",
            command=predict_class
        ).grid(row=len(fields), column=0, columnspan=2, pady=20)

    def process_natural_language(self) -> None:
        """处理自然语言输入"""
        text = self.natural_language_entry.get().strip()

        if not text:
            messagebox.showwarning("输入为空", "请输入指令")
            return

        # 处理上下文
        processed_text = self.dialog_context.process_with_context(text)

        # 解析意图
        operation, params = self.nlp.parse_intent(processed_text)

        # 根据操作执行相应功能
        result = None
        response = ""

        if operation == 'add':
            # 验证参数
            existing_ids = [s.student_id for s in self.student_manager.get_all_students()]
            valid, msg = Validator.validate_all(params, existing_ids)

            if not valid:
                response = f"❌ 添加失败：{msg}"
            else:
                # 创建学生对象
                student = Student(
                    student_id=params.get('student_id', ''),
                    name=params.get('name', ''),
                    age=params.get('age', 18),
                    gender=params.get('gender', '男'),
                    class_name=params.get('class_name', '一班'),
                    phone=params.get('phone', '')
                )

                # 添加学生
                success = self.student_manager.add_student(student)
                result = success
                response = self.nlp.format_response(operation, success, params)

                if success:
                    # 重新训练预测模型
                    self.predictor.train(self.student_manager.get_all_students())

        elif operation == 'update':
            student_id = params.get('student_id')
            if not student_id:
                response = "❌ 更新失败：未提供学号"
            else:
                # 移除student_id，保留更新字段
                update_params = {k: v for k, v in params.items() if k != 'student_id'}

                if update_params:
                    success = self.student_manager.update_student(student_id, **update_params)
                    result = success
                    response = self.nlp.format_response(operation, success, params)

                    if success:
                        # 重新训练预测模型
                        self.predictor.train(self.student_manager.get_all_students())
                else:
                    response = "❌ 更新失败：未提供更新字段"

        elif operation == 'delete':
            student_id = params.get('student_id')
            if student_id:
                success = self.student_manager.delete_student(student_id)
                result = success
                response = self.nlp.format_response(operation, success, params)

                if success:
                    # 重新训练预测模型
                    self.predictor.train(self.student_manager.get_all_students())
            else:
                response = "❌ 删除失败：未提供学号"

        elif operation == 'query':
            query_type = params.get('query_type', 'condition')

            if query_type == 'exact':
                student = self.student_manager.get_student(params.get('student_id', ''))
                result = student
                response = self.nlp.format_response(operation, student, params)

            else:  # 条件查询
                students = self.student_manager.get_students_by_conditions(**params)
                result = students
                response = self.nlp.format_response(operation, students, params)

        elif operation == 'statistics':
            stat_type = params.get('stat_type', 'report')

            if stat_type == 'count':
                students = self.student_manager.get_all_students()
                result = StatisticsAnalyzer.count_by_conditions(students, **params)
                response = result
            elif stat_type == 'class_count':
                students = self.student_manager.get_all_students()
                result = StatisticsAnalyzer.generate_report(students)
                response = result
            else:
                students = self.student_manager.get_all_students()
                result = StatisticsAnalyzer.generate_report(students)
                response = result

        else:
            response = "❓ 无法识别您的指令，请尝试以下格式：\n" \
                       "  • 添加学生李四，学号2023002，年龄19，男生，三班，电话13812345678\n" \
                       "  • 把学号2023001的班级改成一班\n" \
                       "  • 查询二班年龄在18-20岁之间的女生有多少人？\n" \
                       "  • 删除学号2023003的学生"

        # 显示结果
        self.append_result(f"💬 用户输入: {text}\n{response}")

        # 记录到对话上下文
        self.dialog_context.add_to_history(text, response, result)

        # 清空输入框
        self.natural_language_entry.delete(0, tk.END)

        # 更新状态
        self.status_var.set(f"已处理自然语言指令: {operation}")

    def append_result(self, text: str) -> None:
        """向结果区域追加文本"""
        self.result_text.insert(tk.END, text + "\n\n")
        self.result_text.see(tk.END)

    def clear_result(self) -> None:
        """清空结果区域"""
        self.result_text.delete(1.0, tk.END)

    def reset_interface(self) -> None:
        """重置界面"""
        self.clear_result()
        self.natural_language_entry.delete(0, tk.END)
        self.current_mode = "menu"
        self.status_var.set("就绪")
        self.append_result("✨ 界面已重置\n请选择操作或输入自然语言指令")

    def on_closing(self) -> None:
        """关闭程序时的处理"""
        # 保存数据
        self.student_manager.save_data()
        self.root.destroy()
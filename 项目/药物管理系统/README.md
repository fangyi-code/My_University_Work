## 药物管理系统（sms）

这是一个基于 Django 开发的药物管理系统，目前为**本地开发完成、尚未部署到 Linux 的版本**。系统主要用于帮助管理药品信息、库存及相关业务流程，适合在学习、课程设计或小型项目中使用。

- **主要功能：**
  - **药品信息管理**：新增 / 编辑 / 删除药品，管理药品名称、规格、生产厂家、有效期等信息。
  - **库存管理**：记录药品入库、出库和当前库存数量，支持简单的库存查询。
  - **查询与检索**：按药品名称、类别等条件快速查询。
  - **基础权限/账户**（如果有实现）：登录后才能进行管理操作，区分普通用户和管理员。

- **技术栈：**
  - **后端**：Django（Python）
  - **数据库**：默认使用 Django 自带的数据库配置（如 SQLite）
  - **前端**：Django 模板 + 基本的 HTML/CSS/JavaScript

- **运行环境（开发版）：**
  - Python 3.x
  - Django（版本以 `requirements.txt` 或 `settings.py` 为准）
  - 本地开发模式（`DEBUG = True`），尚未进行 Linux 服务器部署与生产环境配置

- **本地运行方式（示例）：**

  1. 创建并激活虚拟环境（可选但推荐）  
     ```bash
     python -m venv venv
     source venv/bin/activate  # Windows 使用 venv\Scripts\activate
     ```
  2. 安装依赖（如果有 `requirements.txt`）：  
     ```bash
     pip install -r requirements.txt
     ```
  3. 数据库迁移：  
     ```bash
     python manage.py migrate
     ```
  4. 启动开发服务器：  
     ```bash
     python manage.py runserver
     ```
  5. 浏览器访问 `http://127.0.0.1:8000/` 使用系统。

- **后续计划（可选）：**
  - 配置并部署到 Linux 服务器（如使用 Gunicorn + Nginx）
  - 完善权限控制、日志记录和异常处理
  - 美化前端界面，提升用户体验


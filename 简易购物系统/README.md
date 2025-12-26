# 购物系统 Web 版

## 安装依赖

### macOS/Linux:
```bash
pip install -r requirements.txt
```

### Windows:
```bash
pip install Flask pymysql
```

或者使用 requirements.txt:
```bash
pip install -r requirements.txt
```

## 运行程序

```bash
python app.py
```

或者：

```bash
python3 app.py
```

然后在浏览器中访问：http://127.0.0.1:5000

**注意：** 确保MySQL服务已启动，并且数据库配置正确。

## 功能说明

1. **浏览商品** - 查看所有商品列表
2. **加入购物车** - 选择商品和数量加入购物车
3. **查看购物车** - 查看购物车中的所有商品
4. **修改购物车** - 修改购物车中商品的数量
5. **删除购物车商品** - 从购物车中删除商品
6. **结账** - 完成购买，更新库存并清空购物车

## 数据库配置

默认配置在 `app.py` 中：

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'luoyu2004918',
    'charset': 'utf8mb4'
}
```

如需修改，请编辑 `app.py` 文件中的 `DB_CONFIG` 变量。


# 使用前请先安装: pip install flask pymysql
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pymysql
from functools import wraps

app = Flask(__name__)
app.secret_key = 'shopping_system_secret_key'

# 数据库连接配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'luoyu2004918',
    'charset': 'utf8mb4'
}

def get_db_connection():
    """获取数据库连接"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        conn.select_db('ShoppingMS')
        return conn
    except pymysql.Error as e:
        flash(f'数据库连接失败: {e}', 'error')
        return None

def init_database():
    """初始化数据库和表"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS ShoppingMS")
        cursor.execute("USE ShoppingMS")
        
        # 商品表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Product(
                商品编号 CHAR(5) PRIMARY KEY,
                商品名称 VARCHAR(30) NOT NULL,
                价格 DECIMAL(8,2) NOT NULL,
                库存 INT DEFAULT 0
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """)
        
        # 购物车表
        cursor.execute("DROP TABLE IF EXISTS Cart")
        cursor.execute("""
            CREATE TABLE Cart(
                商品编号 CHAR(5) PRIMARY KEY,
                商品名称 VARCHAR(30) NOT NULL,
                单价 DECIMAL(8,2) NOT NULL,
                数量 INT NOT NULL,
                小计 DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (商品编号) REFERENCES Product(商品编号)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """)
        
        # 清空数据
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("DELETE FROM Product")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        # 插入示例商品
        products = [
            ('P001', '苹果', 8.50, 100),
            ('P002', '香蕉', 6.00, 80),
            ('P003', '牛奶', 12.00, 50),
            ('P004', '面包', 15.00, 60),
            ('P005', '鸡蛋', 9.90, 120)
        ]
        for p in products:
            cursor.execute("INSERT INTO Product VALUES(%s, %s, %s, %s)", p)
        
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"初始化数据库失败: {e}")
        return False

@app.route('/')
def index():
    """首页 - 浏览商品"""
    conn = get_db_connection()
    if not conn:
        return render_template('error.html', message='数据库连接失败')
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # 转换为字典列表
        product_list = []
        for p in products:
            product_list.append({
                'id': p[0],
                'name': p[1],
                'price': float(p[2]),
                'stock': p[3]
            })
        
        return render_template('index.html', products=product_list)
    except Exception as e:
        conn.close()
        flash(f'查询商品列表时出错: {e}', 'error')
        return render_template('index.html', products=[])

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """加入购物车"""
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 0))
    
    if quantity <= 0:
        flash('数量必须大于0！', 'error')
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('index'))
    
    try:
        cursor = conn.cursor()
        
        # 查询商品信息
        cursor.execute("SELECT * FROM Product WHERE 商品编号=%s", (product_id,))
        product = cursor.fetchone()
        
        if not product:
            flash('商品不存在！', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('index'))
        
        if quantity > product[3]:
            flash(f'库存不足！当前库存：{product[3]}', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('index'))
        
        price = float(product[2])
        subtotal = price * quantity
        
        # 检查购物车中是否已有该商品
        cursor.execute("SELECT * FROM Cart WHERE 商品编号=%s", (product_id,))
        cart_item = cursor.fetchone()
        
        if cart_item:
            new_quantity = cart_item[3] + quantity
            if new_quantity > product[3]:
                flash(f'购物车中已有{cart_item[3]}件，再加{quantity}件超过库存！', 'error')
                cursor.close()
                conn.close()
                return redirect(url_for('index'))
            new_subtotal = price * new_quantity
            cursor.execute("UPDATE Cart SET 数量=%s, 小计=%s WHERE 商品编号=%s", 
                         (new_quantity, new_subtotal, product_id))
        else:
            cursor.execute("INSERT INTO Cart VALUES(%s, %s, %s, %s, %s)",
                         (product_id, product[1], price, quantity, subtotal))
        
        conn.commit()
        flash(f'已添加 {quantity} 件 {product[1]} 到购物车！', 'success')
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        conn.rollback()
        conn.close()
        flash(f'添加购物车时出错: {e}', 'error')
        return redirect(url_for('index'))

@app.route('/cart')
def cart():
    """查看购物车"""
    conn = get_db_connection()
    if not conn:
        return render_template('error.html', message='数据库连接失败')
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cart")
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # 转换为字典列表
        cart_items = []
        total = 0
        for item in items:
            cart_items.append({
                'id': item[0],
                'name': item[1],
                'price': float(item[2]),
                'quantity': item[3],
                'subtotal': float(item[4])
            })
            total += float(item[4])
        
        return render_template('cart.html', items=cart_items, total=total)
    except Exception as e:
        conn.close()
        flash(f'查询购物车时出错: {e}', 'error')
        return render_template('cart.html', items=[], total=0)

@app.route('/update_cart', methods=['POST'])
def update_cart():
    """修改购物车商品数量"""
    product_id = request.form.get('product_id')
    new_quantity = int(request.form.get('quantity', 0))
    
    if new_quantity <= 0:
        flash('数量必须大于0！', 'error')
        return redirect(url_for('cart'))
    
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('cart'))
    
    try:
        cursor = conn.cursor()
        
        # 检查购物车中是否有该商品
        cursor.execute("SELECT * FROM Cart WHERE 商品编号=%s", (product_id,))
        cart_item = cursor.fetchone()
        
        if not cart_item:
            flash('购物车中无此商品！', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('cart'))
        
        # 检查库存
        cursor.execute("SELECT 库存 FROM Product WHERE 商品编号=%s", (product_id,))
        stock = cursor.fetchone()[0]
        
        if new_quantity > stock:
            flash(f'库存不足！当前库存：{stock}', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('cart'))
        
        # 更新购物车
        new_subtotal = float(cart_item[2]) * new_quantity
        cursor.execute("UPDATE Cart SET 数量=%s, 小计=%s WHERE 商品编号=%s",
                     (new_quantity, new_subtotal, product_id))
        
        conn.commit()
        flash('修改成功！', 'success')
        cursor.close()
        conn.close()
        return redirect(url_for('cart'))
    except Exception as e:
        conn.rollback()
        conn.close()
        flash(f'修改购物车时出错: {e}', 'error')
        return redirect(url_for('cart'))

@app.route('/delete_cart/<product_id>')
def delete_cart(product_id):
    """删除购物车商品"""
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('cart'))
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Cart WHERE 商品编号=%s", (product_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            flash('删除成功！', 'success')
        else:
            flash('购物车中无此商品！', 'error')
        
        cursor.close()
        conn.close()
        return redirect(url_for('cart'))
    except Exception as e:
        conn.rollback()
        conn.close()
        flash(f'删除购物车商品时出错: {e}', 'error')
        return redirect(url_for('cart'))

@app.route('/checkout', methods=['POST'])
def checkout():
    """结账"""
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('cart'))
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cart")
        items = cursor.fetchall()
        
        if not items:
            flash('购物车为空，无法结账！', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('cart'))
        
        # 更新库存并清空购物车
        for item in items:
            cursor.execute("UPDATE Product SET 库存=库存-%s WHERE 商品编号=%s",
                         (item[3], item[0]))
        
        cursor.execute("DELETE FROM Cart")
        conn.commit()
        
        # 计算总金额
        total = sum(float(item[4]) for item in items)
        
        cursor.close()
        conn.close()
        flash(f'结账成功！支付金额：{total:.2f}元', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        conn.rollback()
        conn.close()
        flash(f'结账时出错: {e}', 'error')
        return redirect(url_for('cart'))

if __name__ == '__main__':
    # 初始化数据库
    print("正在初始化数据库...")
    if init_database():
        print("数据库初始化成功！")
    else:
        print("数据库初始化失败，请检查配置")
    
    # 启动Web服务器
    print("启动Web服务器...")
    port = 5001  # 使用5001端口，避免与macOS AirPlay Receiver冲突
    print(f"访问地址: http://127.0.0.1:{port}")
    app.run(debug=True, host='0.0.0.0', port=port)


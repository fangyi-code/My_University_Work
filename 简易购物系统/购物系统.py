# 使用前请先安装pymysql: pip install pymysql
# 如果遇到安装问题，可以使用: pip install --break-system-packages pymysql
import pymysql
import sys
import os

# Windows系统设置控制台编码为UTF-8
if sys.platform == 'win32':
    try:
        os.system('chcp 65001 > nul')  # 设置代码页为UTF-8
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except:
        pass

# 数据库连接配置
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'luoyu2004918',
    'charset': 'utf8mb4'
}

connection = None
cursor = None

try:
    connection = pymysql.connect(**config)
    cursor = connection.cursor()
except pymysql.Error as e:
    print(f"数据库连接失败: {e}")
    print("\n请检查：")
    print("1. MySQL服务是否已启动")
    print("2. 数据库用户名和密码是否正确")
    print("3. 是否已安装pymysql: pip install pymysql")
    sys.exit(1)

try:
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
    
    connection.commit()
    
    print("=" * 50)
    print("欢迎来到购物系统！")
    print("=" * 50)
    
    while True:
        print("\n1. 浏览商品")
        print("2. 加入购物车")
        print("3. 查看购物车")
        print("4. 修改购物车")
        print("5. 删除购物车商品")
        print("6. 结账")
        print("0. 退出")
        
        choice = input("\n请选择功能：").strip()
        
        if choice == '1':
            try:
                print("\n商品列表：")
                cursor.execute("SELECT * FROM Product")
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        print(f"编号:{row[0]} 名称:{row[1]} 价格:{row[2]}元 库存:{row[3]}")
                else:
                    print("暂无商品")
            except Exception as e:
                print(f"查询商品列表时出错: {e}")
        
        elif choice == '2':
            product_id = input("请输入商品编号：").strip()
            cursor.execute("SELECT * FROM Product WHERE 商品编号=%s", (product_id,))
            product = cursor.fetchone()
            if not product:
                print("商品不存在！")
                continue
            
            try:
                quantity = int(input("请输入数量："))
                if quantity <= 0:
                    print("数量必须大于0！")
                    continue
            except ValueError:
                print("请输入有效的数字！")
                continue
            
            if quantity > product[3]:
                print(f"库存不足！当前库存：{product[3]}")
                continue
            
            price = float(product[2])
            subtotal = price * quantity
            
            cursor.execute("SELECT * FROM Cart WHERE 商品编号=%s", (product_id,))
            cart_item = cursor.fetchone()
            
            if cart_item:
                new_quantity = cart_item[3] + quantity
                if new_quantity > product[3]:
                    print(f"购物车中已有{cart_item[3]}件，再加{quantity}件超过库存！")
                    continue
                new_subtotal = price * new_quantity
                cursor.execute("UPDATE Cart SET 数量=%s, 小计=%s WHERE 商品编号=%s", 
                             (new_quantity, new_subtotal, product_id))
            else:
                cursor.execute("INSERT INTO Cart VALUES(%s, %s, %s, %s, %s)",
                             (product_id, product[1], price, quantity, subtotal))
            
            connection.commit()
            print(f"已添加 {quantity} 件 {product[1]} 到购物车！")
        
        elif choice == '3':
            print("\n购物车：")
            cursor.execute("SELECT * FROM Cart")
            items = cursor.fetchall()
            if not items:
                print("购物车为空！")
            else:
                total = 0
                for item in items:
                    print(f"编号:{item[0]} 名称:{item[1]} 单价:{item[2]}元 数量:{item[3]} 小计:{item[4]}元")
                    total += float(item[4])
                print(f"\n总计：{total:.2f}元")
        
        elif choice == '4':
            product_id = input("请输入要修改的商品编号：").strip()
            cursor.execute("SELECT * FROM Cart WHERE 商品编号=%s", (product_id,))
            cart_item = cursor.fetchone()
            if not cart_item:
                print("购物车中无此商品！")
                continue
            
            cursor.execute("SELECT 库存 FROM Product WHERE 商品编号=%s", (product_id,))
            stock = cursor.fetchone()[0]
            
            try:
                new_quantity = int(input(f"当前数量：{cart_item[3]}，请输入新数量："))
                if new_quantity <= 0:
                    print("数量必须大于0！")
                    continue
            except ValueError:
                print("请输入有效的数字！")
                continue
            
            if new_quantity > stock:
                print(f"库存不足！当前库存：{stock}")
                continue
            
            new_subtotal = float(cart_item[2]) * new_quantity
            cursor.execute("UPDATE Cart SET 数量=%s, 小计=%s WHERE 商品编号=%s",
                         (new_quantity, new_subtotal, product_id))
            connection.commit()
            print("修改成功！")
        
        elif choice == '5':
            product_id = input("请输入要删除的商品编号：").strip()
            cursor.execute("DELETE FROM Cart WHERE 商品编号=%s", (product_id,))
            if cursor.rowcount > 0:
                connection.commit()
                print("删除成功！")
            else:
                print("购物车中无此商品！")
        
        elif choice == '6':
            cursor.execute("SELECT * FROM Cart")
            items = cursor.fetchall()
            if not items:
                print("购物车为空，无法结账！")
                continue
            
            print("\n购物清单：")
            total = 0
            for item in items:
                print(f"{item[1]} × {item[3]} = {item[4]}元")
                total += float(item[4])
            
            print(f"\n总计金额：{total:.2f}元")
            confirm = input("\n确认结账？(y/n)：").strip()
            
            if confirm == 'y':
                for item in items:
                    cursor.execute("UPDATE Product SET 库存=库存-%s WHERE 商品编号=%s",
                                 (item[3], item[0]))
                cursor.execute("DELETE FROM Cart")
                connection.commit()
                print(f"\n结账成功！支付金额：{total:.2f}元")
                print("感谢您的购物，再见！")
                break
        
        elif choice == '0':
            print("感谢使用，再见！")
            break
        
        else:
            print("无效选择，请重新输入！")

except Exception as e:
    print(f"发生错误: {e}")
    if connection:
        connection.rollback()
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()


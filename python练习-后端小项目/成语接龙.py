chengyu_list = ['万事如意','发奋图强','笑容满面','意气风发','强颜欢笑']
print('万事如意')

# 目前在使用的成语
be_used = '万事如意'
# 还剩下的成语，列表推导式更加美观优雅
remain_str = [x for x in chengyu_list if x != be_used]

while True:
    for i in remain_str:
        last = be_used[-1]
        if i[0] == last:
            # 修改
            be_used = i
            # remove可以精准删除第一个匹配到的字符
            remain_str.remove(i)
            print(" ")
            print(i)

#生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中.
import string,pymysql
from random import randint
s_low=string.ascii_lowercase
s_up=string.ascii_uppercase
s_num="0123456789"
def key_create(num):
    key=[]
    for i in range(num):
        keys=""
        for j in range(1,17):
            choice=randint(1,5)
            if choice==1:
                s=randint(0,9)
                keys +=s_num[s]
            elif 2<=choice<4:
                s=randint(0,25)
                keys +=s_low[s]
            else:
                s=randint(0,25)
                keys +=s_up[s]
            if j%4==0 and j!=16:
                keys +="-"
        key.append(keys)
    return key
Key=key_create(200)
# change root passw
conn = pymysql.connect(  user='root',  passwd='passward', db='test', charset='utf8')
cursor = conn.cursor()
# 创建user表:
cursor.execute("DROP TABLE IF EXISTS user")
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
for k in range(0,200):
    cursor.execute('insert into user (id, name) values (%s, %s)', (k+1, Key[k]))
#print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
for kk in range(0,200):
    cursor.execute('select * from user where id = %s', (kk+1),)
    values = cursor.fetchall()
    print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()


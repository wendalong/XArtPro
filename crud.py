import pymysql

params = {
   'host':'127.0.0.1',
   'port': 3306,
   'user': 'root',
   'password': 'root',
   'db': 'mysql',
   'charset': 'utf8'
}

conn = pymysql.Connect(**params)
print('-连接成功--')

cursor = conn.cursor()
cursor.execute('desc user')
for row in cursor.fetchall():
    print(row)

print('--关闭数据库--')
cursor.close()
conn.close()

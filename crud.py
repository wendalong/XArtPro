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


print('-创建数据库artdb--')
# cursor.execute('create database artdb')
# cursor.execute('create table artdb.tag (id integer primary key auto_increment, name varchar(50) unique)')

cursor.execute("insert artdb.tag(name) values ('军事小说'),('都市言情')")
conn.commit()
print(cursor.rownumber)

print('--关闭数据库--')
cursor.close()
conn.close()

import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysql',database='MovieDataBase')
cur = conn.cursor()
cur.execute('create table user_table(userid varchar(25) primary key,passwrd varchar(25) not null )')
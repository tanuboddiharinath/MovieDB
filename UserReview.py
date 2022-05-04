import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysql',database='MovieDataBase')
cur = conn.cursor()
cur.execute('create table user_review(Movie_Title varchar(60),userid varchar(5),review varchar(100))')
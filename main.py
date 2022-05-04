import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysql',database='MovieDataBase')
cur = conn.cursor()
#cur.execute('create table user_table(userId varchar(25) primary key,passwrd varchar(25) not null )')
print('MovieDataBase')
import datetime as dt
print(dt.datetime.now())
print('3.Admin')
print()
print('')
print('1.User_REGISTER')
print()
print('2.User_LOGIN')
print()



n=int(input('enter your choice='))
print()
if n == 3:
     Admin = input("UserId: ")
     print()
     Password = input("Password: ")
     print()
     admin_query="select * from user_table where passwrd='"+str(Password)+"' and userId=  ' " +Password+ " ' "
     cur.execute(admin_query)
     if cur.fetchone() is  None:
          print()
          print('Invalid Admin_Id or password')
     else:
          print()
          import Adminmenu



if n== 1:
     userid=input('Enter a UserId=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     V_SQLInsert="INSERT  INTO user_table (passwrd,userId) values (" +  str (passwd) + ",' " + userid + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import Usermenu

if  n==2 :
     userid=input('Enter your UserId=')
     print()
     passwd=int(input('Enter your 4 DIGIT Password='))
     V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and userId=  ' " +userid+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import Usermenu
import main
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysql',database='MovieDataBase')
cur = conn.cursor()

conn.autocommit = True
c = 'yes'
while c == 'yes':
    print("User_ID ",main.userid)
    print()
    print('1.Give_Rating')
    print()
    print('2.Give_Review')
    print()
    print('3.Search Movie Rating')
    print()
    print('4.Quit')
    n = int(input('Enter your CHOICE='))
    print()

    if n == 1:
        moviename = input("Enter the movie name: ")
        print()
        cur.execute('select * from movie where Title like "%{}%"'.format(moviename))
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()
        if count == 0:
            print()
            print("Sorry we don't have the movie you have Searched")
        else:
            rating = input(" Enter the Rating :")
            # V_SQLInsert="INSERT  INTO user_rating (Movie_Title,userid,rating) values (" +  str (moviename) + ",' " + main.userid + ",' " + rating + " ') "
            V_SQLInsert="INSERT  INTO user_rating values ('{}' , '{}' , '{}' ) ".format(moviename,main.userid,rating)
            cur.execute(V_SQLInsert)
            # cur.execute("INSERT INTO user_rating(Movie_Title,userid,rating) values ("+ moviename + "," + main.userid + "," + rating + ")")
            # cur.execute(query)
            conn.commit()

    if n == 2:
        moviename = input('Enter MovieName to give review =')
        print()
        cur.execute('select * from movie where Title like "%{}%"'.format(moviename))
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()
        if count == 0:
            print()
            print("Sorry we don't have the movie you have Searched")
        else:
            review = input(" Enter the Review :")
            V_SQLInsert="INSERT  INTO user_review values ('{}' , '{}' , '{}' ) ".format(moviename,main.userid,review)
            cur.execute(V_SQLInsert)
            conn.commit()


    if n == 3:
        moviename = input('Enter MovieName To Get Details =')
        Q_Search = ('select * from movie where Title like "%{}%"'.format(moviename))
        cur.execute(Q_Search)
        data = cur.fetchall()
        print(data)
        count = cur.rowcount
        conn.commit()
    if n == 4:
        print("""""")
    if n == 5:
        break
        
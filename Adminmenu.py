import main

import main
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysql',database='MovieDataBase')
cur = conn.cursor()

conn.autocommit = True
c = 'y'
while c == 'y':
    print('1.Update')
    print()
    print('2.Insert')
    print()
    print('3.Delete')
    print()
    print('4.Change Admin Info')
    print()
    print('5.Quit')

    n = int(input("Enter the Choice: "))
    if n == 1:
        moviename = input("Enter the MovieName: ")
        Update_Query = "select * from movie where Title =' "+ moviename+"'"
        cur.execute(Update_Query)
        data = cur.fetchall()
        count = cur.rowcount
        if count is None:
            print("The movie you searched doesn't exist in our DataBase")
        else:
            print("""1.Year
                    2.Title
                    3.Description
                    4.Duration
                    5.Genre
                    6.Rating
                    7.MetaScore
                    8.Votes
                    9.Gross_Earnings_In_Mil
                    10.Director
                    11.Actor""")
            sel = int(input("Please Enter the Choise: "))
            if sel == 1:
                year = input()
                up_query = 'UPDATE movie SET year ='+year+' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 2:
                Title = input()
                up_query = 'UPDATE movie SET Title =' + Title +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 3:
                Description = input()
                moviename = input("Enter the MovieName Where You could like to Update")
                up_query = 'UPDATE movie SET Description =' + Description +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 4:
                Duration = int(input())
                up_query = 'UPDATE movie SET Duration =' + Duration +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 5:
                genre = input()
                up_query = 'UPDATE movie SET genre =' + genre +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 6:
                Rating = float(input())
                moviename = input("Enter the MovieName Where You could like to Update")
                up_query = 'UPDATE movie SET Rating =' + Rating +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 7:
                Metascore = int(input())
                up_query = 'UPDATE movie SET Metascore =' + Metascore +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 8:
                votes = int(input())
                up_query = 'UPDATE movie SET votes =' + votes +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 9:
                Gross_Earnings = float(input())
                up_query = 'UPDATE movie SET Gross_Earning_in_Mil =' + Gross_Earnings +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 10:
                Director = input()
                moviename = input("Enter the MovieName Where You could like to Update")
                up_query = 'UPDATE movie SET Director =' + Director +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
            if sel == 11:
                Actor = input()
                moviename = input("Enter the MovieName Where You could like to Update")
                up_query = 'UPDATE movie SET Actor =' + Actor +' WHERE Title like "%{}%"'.format(moviename)
                cur.execute(up_query)
                conn.commit()
    if n == 2:
        moviename = input("Enter the MovieName: ")
        Update_Query = "select * from movie where Title =' " + moviename + "'"
        cur.execute(Update_Query)
        data = cur.fetchall()
        count = cur.rowcount
        if count is None:
            print("The movie you searched doesn't exist in our DataBase")
        else:
            year = input()
            title = input()
            description = input()
            duration = input()
            genre = input()
            rating = input()
            metascore = input()
            votes = input()
            gross_earnings = input()
            director = input()
            actor = input()
            insert_query = 'insert into table movie values('+ year + "," + title + "," + description + "," \
                       + duration + "," + genre + "," + rating + "," + metascore + ","\
                       + votes + "," + gross_earnings + "," + director + "," + actor+ ")"
            cur.execute(insert_query)
            conn.commit()
    if n == 3:
        moviename = input("Enter the MovieName: ")
        Update_Query = "select * from movie where Title =' " + moviename + "'"
        cur.execute(Update_Query)
        data = cur.fetchall()
        count = cur.rowcount
        if count is None:
            print("The movie you searched doesn't exist in our DataBase")
        else:
            del_query = 'delect * from movie where title ='+ moviename
    if n == 4:
        print("""""")
    if n == 5:
        break



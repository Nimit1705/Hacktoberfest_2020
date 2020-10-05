import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="dheeraj",passwd="mandvi",database="student")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE student(Rollno int(3),Name varchar(15),Marks int(4))")

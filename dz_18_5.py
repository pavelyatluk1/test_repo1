# Pavlo Yatluk
# dz_18
# 5. Напишіть програму, яка додає до таблиці "student" дані (01, "John"),
# а до таблиці "employee" - (01, "John", 10000)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavel18",
    database="my_firs_db"
)

mycursor = mydb.cursor()
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ("01", "John")
mycursor.execute(sql, val)
mydb.commit()

mycursor = mydb.cursor()
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = ("01", "John", "10000")
mycursor.execute(sql, val)
mydb.commit()


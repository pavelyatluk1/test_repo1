# Pavlo Yatluk
# dz_18
# 2. Напишіть програму, яка створить у базі "my_firs_db" таблицю "student" з полями "id" (INT)
# і "name" (VARCHAR(255)).

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavel18",
    database="my_firs_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

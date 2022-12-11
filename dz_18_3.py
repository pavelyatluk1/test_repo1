# Pavlo Yatluk
# dz_18
# 3. Напишіть програму, яка створить у базі "my_firs_db" таблицю "employee" з полями "id" (INT ATUO_INCREMENT
# PRIMARY KEY), "name" (VARCHAR(255)) і "salary" (INT(6)).

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavel18",
    database="my_firs_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")
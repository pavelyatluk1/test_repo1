# Pavlo Yatluk
# dz_18
# 4. Напишіть програму, яка змінить у таблиці "student" полe "id" на PRIMARY KEY.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavel18",
    database="my_firs_db"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student MODIFY id INT AUTO_INCREMENT PRIMARY KEY")
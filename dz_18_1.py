# Pavlo Yatluk
# dz_18
# 1. Напишіть програму, яка створює нову базу даних "my_firs_db".

# Creating a Database

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavel18"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_firs_db")

# Create connection
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavel18",
    database="my_firs_db"
)

print(mydb)

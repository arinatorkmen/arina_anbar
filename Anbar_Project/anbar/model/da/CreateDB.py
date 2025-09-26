import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE anbar")
db.close()

# cursor.execute("DROP DATABASE IF EXISTS anbar")  # حذف دیتابیس

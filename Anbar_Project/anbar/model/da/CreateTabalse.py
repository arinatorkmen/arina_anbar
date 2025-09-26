import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="anbar")

cursor = db.cursor()

cursor.execute("CREATE TABLE PERSON (id INT AUTO_INCREMENT PRIMARY KEY, PCode VARCHAR(255), FName VARCHAR(255),"
               "LName VARCHAR(255), PBirth_Date VARCHAR(255), PRole VARCHAR(255), PStatus VARCHAR(255))")

cursor.execute("CREATE TABLE STUFF (id INT AUTO_INCREMENT PRIMARY KEY, PCode VARCHAR(255), FName VARCHAR(255),"
               "PUint VARCHAR(255), PCount VARCHAR(255), Price VARCHAR(255), PStatus VARCHAR(255))")
db.commit()
db.close()

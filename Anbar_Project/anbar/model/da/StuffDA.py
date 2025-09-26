import mysql.connector


class StuffDA:
    def __init__(self):
        print("Stuff Data Access")
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="anbar")
        self.cursor = self.db.cursor()

    def add(self, stuff):
        sql_command = "INSERT INTO STUFF (PCode, FName, PUint, PCount, Price, PStatus) values (%s,%s,%s,%s,%s,%s)"
        data = [stuff.code, stuff.name, stuff.unit, stuff.count, stuff.price, 1]
        self.cursor.execute(sql_command, data)
        self.db.commit()
        self.close()

    def edit(self, stuff):
        sql_command = "UPDATE STUFF SET FName=%s,PUint=%s,PCount=%s,Price=%s WHERE PCode=%s"
        data = [stuff.code, stuff.name, stuff.unit, stuff.count, stuff.price]
        self.cursor.execute(sql_command, data)
        self.db.commit()
        self.close()

    def remove(self, code):
        sql_command = "UPDATE STUFF SET PStatus = 0 WHERE PCode=%s"
        data = [code]
        self.cursor.execute(sql_command, data)
        self.db.commit()
        self.close()

    def show_all(self):
        pass

    def close(self):
        self.cursor.close()
        self.db.close()

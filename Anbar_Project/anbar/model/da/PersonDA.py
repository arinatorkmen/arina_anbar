import mysql.connector


class PersonDA:
    def __init__(self):
        print("Person Data Access")
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="anbar")
        self.cursor = self.db.cursor()

    def add(self, person):
        sql_command = "INSERT INTO PERSON (PCode, FName, LName, PBirth_Date, PRole, PStatus) values (%s,%s,%s,%s,%s,%s)"
        data = [person.code, person.name, person.family, person.birth_date, person.role, 1]
        self.cursor.execute(sql_command, data)
        self.db.commit()
        self.show_all()
        self.close()

    def edit(self, person):
        sql_command = "UPDATE PERSON SET FName=%s,LName=%s,PBirth_Date=%s,PRole=%s WHERE PCode=%s"
        data = [person.code, person.name, person.family, person.birth_date, person.role]
        self.cursor.execute(sql_command, data)
        self.db.commit()
        self.close()

    def remove(self, code):
        sql_command = "UPDATE PERSON SET PStatus = 0 WHERE PCode=%s"
        data = [code]
        self.cursor.execute(sql_command, data)
        self.db.commit()
        self.close()

    def show_all(self):
        self.cursor.execute("SELECT * From PERSON")
        result = self.cursor.fetchall()

        for person in result:
            print(person)

    def close(self):
        self.cursor.close()
        self.db.close()

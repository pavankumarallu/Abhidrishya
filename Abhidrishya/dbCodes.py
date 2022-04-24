import mysql.connector


class CriminalRecord:
    def __init__(self,fileName):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pavan@123",
            database="criminaldata"
        )
        self.fileName = fileName
    
    def fetch_name_age(self):
        cursorObject = self.mydb.cursor()
        query = """SELECT Name,Age FROM data where Filename IN (%s)"""
        fil = [self.fileName]
        cursorObject.execute(query,fil)
        myresult = cursorObject.fetchall()
        return myresult
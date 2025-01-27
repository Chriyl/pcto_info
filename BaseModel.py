from flask_mysqldb import MySQL

mysql = MySQL()

cursor = mysql.connection.cursor()

class BaseModel:
    def __init__(self, table_name, db: Database):
        self.table_name = table_name
        self.db = db

    def getAll(self) ->tuple:
        dati: tuple[tuple] 
        try:
            with cursor as self.db.getConn().cursor():
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                dati = cursor.fetchall()
                return dati
        except Exception as e:
            print(e)


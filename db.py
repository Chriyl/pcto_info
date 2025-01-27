from flask_mysqldb import MySQL
from BaseModel import BaseModel
import os
from dotenv import load_dotenv
load_dotenv("db.env")

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_DBNAME = os.getenv("MYSQL_DB")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")




class Database:
    def __init__(self, app ):
        
        self.app = app
        self.app.config['MYSQL_HOST'] = DB_HOST
        self.app.config['MYSQL_USER'] = DB_USER
        self.app.config['MYSQL_PASSWORD'] = DB_PASSWORD
        self.app.config['MYSQL_DB'] = DB_DBNAME
        self.app.config['MYSQL_PORT'] = DB_PORT
        self.mysql = MySQL(self.app)

        # Connessione per ottenere le tabelle
        conn = self.mysql.connection
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        cursor.close()

        # Creazione dinamica dei modelli per ogni tabella
        for (table_name,) in tables:
            setattr(self, table_name, BaseModel(self, table_name))
    
    def getConn(self):
        return self.mysql.connection



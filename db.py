from flask_mysqldb import MySQL
import os
from typing import TYPE_CHECKING
from dotenv import load_dotenv
load_dotenv("db.env")

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_DBNAME = os.getenv("MYSQL_DB")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = int(os.getenv("MYSQL_PORT"))







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
            print(f"tabella trovata: {table_name}")
            setattr(self, table_name, BaseModel(table_name, self)) 
    
    def getConn(self):
        return self.mysql.connection


class BaseModel:
    def __init__(self, table_name, db: Database):
        self.table_name = table_name
        self.db = db

    def getAll(self) -> tuple:
        try:
            conn = self.db.getConn()
            with conn.cursor() as cursor:
                query = f"SELECT * FROM {self.table_name}"
                print(f"Eseguo query: {query}")  
                cursor.execute(query)
                dati = cursor.fetchall()
                print(f"Dati recuperati: {dati}")  
                return dati
        except Exception as e:
            print(f"Errore durante il recupero dei dati: {e}")
            return ()
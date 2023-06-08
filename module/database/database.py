import sqlite3

class database():
    database: sqlite3.Connection
    
    def connectToDb(self):  # Add the self parameter
        try:
            self.dbConnection = sqlite3.connect('gfg.db')
            dbCursor = self.dbConnection.cursor()
            print("Database connected successfully.")
        except:
            print("Database connection failed.")
        
    def closeConnection(self):  # Add the self parameter
        self.database.close()
        print("Database Connection closed.")   
import sqlite3

class database():
    
    def connectToDb(self, db):  # Add the self parameter
        try:
            self.dbConnection = sqlite3.connect(db)
            self.dbCursor = self.dbConnection.cursor()
        
            print("Database connected successfully.") 
            self.dbConnection.commit()
        except:
            print("Database connection failed.")
        
    def closeConnection(self):  # Add the self parameter
        self.dbConnection.close()
        print("Database Connection closed.")   
    
    def executeStatement(self, statement):
        try:
            self.dbCursor.execute(statement)
            self.dbConnection.commit()
            
            print("Statement executed successfully.")
        except:
            print("Statement execution failed.") 
        
    def insertIntoDb(self, statement):
        try:
            self.dbCursor.execute("INSERT INTO errorRequests (requestText) VALUES ?;", statement)
            self.dbConnection.commit()
        except:
            print("Database Insert failed.")   
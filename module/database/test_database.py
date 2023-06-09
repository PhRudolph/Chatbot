import unittest
import sqlite3
from unittest.mock import patch
from io import StringIO

from database import database

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.database = database()
    
    def test_database_connect(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.database.connectToDb("database.db")
            self.assertEqual("Database connected successfully.", output.getvalue().strip())
            
    def test_database_close(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.database.connectToDb("database.db")
            self.database.closeConnection()
            self.assertEqual("Database connected successfully.\nDatabase Connection closed.", 
                             output.getvalue().strip()) 

unittest.main()
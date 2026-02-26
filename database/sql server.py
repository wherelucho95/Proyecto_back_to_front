import pyodbc
from database.base import BaseDatabase

class SQLServerDatabase(BaseDatabase):

    def __init__(self, connection_string: str):
        self._connection = pyodbc.connect(connection_string)
        self._cursor = self._connection.cursor()

    def execute(self, query: str, params: tuple = ()):
        self._cursor.execute(query, params)
        self._connection.commit()

    def fetchall(self):
        return self._cursor.fetchall()

    def close(self):
        self._connection.close()    
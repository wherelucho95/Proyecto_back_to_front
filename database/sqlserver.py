import pyodbc
from database.base import BaseDatabase


class SQLServerDatabase(BaseDatabase):

    def __init__(self, connection_string: str):
        self._connection = pyodbc.connect(connection_string)
        self._cursor = self._connection.cursor()

    def execute(self, query: str, params: tuple = None):
        """
        Ejecuta cualquier query (SELECT, INSERT, UPDATE, DELETE).
        NO hace commit automático.
        """
        if params:
            self._cursor.execute(query, params)
        else:
            self._cursor.execute(query)

    def fetchall(self):
        """
        Devuelve todos los registros del último SELECT ejecutado.
        """
        return self._cursor.fetchall()

    def fetchone(self):
        """
        Devuelve un solo registro.
        """
        return self._cursor.fetchone()

    def commit(self):
        """
        Hace commit manualmente (solo usar en INSERT/UPDATE/DELETE).
        """
        self._connection.commit()

    def close(self):
        self._cursor.close()
        self._connection.close()
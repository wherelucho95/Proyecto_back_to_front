from models.user import User
from database.base import BaseDatabase


class UserRepository:

    def __init__(self, db: BaseDatabase):
        self._db = db

    def create_table(self):
        query = """
        IF NOT EXISTS (
            SELECT * FROM sysobjects WHERE name='users' AND xtype='U'
        )
        CREATE TABLE users (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100)
        )
        """
        self._db.execute(query)

    def add_user(self, user: User):
        query = """
        INSERT INTO users (name, age, email)
        VALUES (?, ?, ?)
        """
        self._db.execute(query, (user.name, user.age, user.email))

    def get_all_users(self):
        query = "SELECT id, name, age, email FROM users"
        self._db.execute(query)
        return self._db.fetchall()

        return [User(row[0], row[1], row[2]) for row in rows]
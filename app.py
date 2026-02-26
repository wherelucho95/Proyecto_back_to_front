from database.sqlserver import SQLServerDatabase
from repository.user_repository import UserRepository
from models.user import User


connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-E4KSP0B;"
    "DATABASE=PythonPOO;"
    "Trusted_Connection=yes;"
)

def main():

    db = SQLServerDatabase(connection_string)
    repo = UserRepository(db)

    repo.create_table()

    name = input("Nombre: ")
    age = int(input("Edad: "))
    email = input("Email: ")

    user = User(name, age, email)
    repo.add_user(user)

    print("\nUsuarios registrados:")
    users = repo.get_all_users()

    for u in users:
        print(u)

    db.close()


if __name__ == "__main__":
    main()
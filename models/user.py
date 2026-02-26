class User:
    def __init__(self, name: str, age: int, email: str):
        self._name = name
        self._age = age
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email

    def __repr__(self):
        return f"User(name={self._name}, age={self._age}, email={self._email})"
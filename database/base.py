from abc import ABC, abstractmethod

class BaseDatabase(ABC):

    @abstractmethod
    def execute(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def fetchall(self):
        pass

    @abstractmethod
    def close(self):
        pass
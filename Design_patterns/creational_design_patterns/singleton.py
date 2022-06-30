"""
Singleton Method is one of the simplest design pattern available to us.
It is a way to provide one and only one object of a particular type.
It involves only one class to create methods and specify the objects.

Singleton Design Pattern can be understood by a very simple example of
Database connectivity. When each object creates a unique Database Connection
to the Database, it will highly affect the cost and expenses of the project.
So, it is always better to make a single connection rather than making extra
irrelevant connections which can be easily done by Singleton Design Pattern.
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    print(logger1 is logger2)

# wrong code
class DbConnectionSingleton:
    _instance = None

    def __init__(self, url, username, password) -> None:
        self.url = url
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return "[ {} - {} - {} ]".format(self.url, self.username, self.password)

    @staticmethod
    def getInstance(self, url, username, password):
        if self._instance == None:
            # if instance is none then only create the new instance
            # self._instance = DbConnectionSingleton("https://db:120.0.01", "username", "password");
            self._instance = DbConnectionSingleton(url, username, password)
        return self._instance
    

# above singleton implementation wont work in python we need to override __new__ method 
# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance

# # Example usage:
# singleton_instance_1 = Singleton()
# singleton_instance_2 = Singleton()

# print(singleton_instance_1 is singleton_instance_2)  # This should print True


# corrected code for singleton db connections
class DbConnectionSingleton:
    _instance = None

    def __init__(self, url, username, password):
        # Ensure that an instance can only be created through getInstance
        raise RuntimeError("Use DbConnectionSingleton.getInstance() to create an instance.")

    def __str__(self):
        return "[ {} - {} - {} ]".format(self.url, self.username, self.password)

    @classmethod
    def getInstance(cls, url, username, password):
        if cls._instance is None:
            """
                On below line we are calling __new__ method on the parent class of DbConnectionSingleton i.e Object
                __new__ is a special method in Python classes that is responsible for creating a new instance of the class. 
                It is a class method and is called before the __init__ method. While __init__ is responsible for initializing 
                the created instance, __new__ is responsible for creating and returning a new instance of the class.
            """
            cls._instance = super(DbConnectionSingleton, cls).__new__(cls) # this will create new obj using default constructor
            """
                So, in the provided line, we're calling the __new__ method of the parent class 
                (super(DbConnectionSingleton, cls).__new__(cls)), and it creates a new instance of the class 
                without invoking the __init__ method. After this line, we manually set the attributes (url, username, password) 
                for the instance.
            """
            cls._instance.url = url
            cls._instance.username = username
            cls._instance.password = password
        return cls._instance

# Example usage:
# db_instance_0 = DbConnectionSingleton("https://db:120.0.189", "zeo_username", "zero_password") # this is throw an error
db_instance_1 = DbConnectionSingleton.getInstance("https://db:120.0.01", "username", "password")
db_instance_2 = DbConnectionSingleton.getInstance("https://anotherdb:3306", "admin", "adminpassword")

print(db_instance_1 is db_instance_2) # This should print True
print(db_instance_1, db_instance_2) # now both instances are referring to same object

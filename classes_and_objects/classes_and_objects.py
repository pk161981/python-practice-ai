#Class
#Class is a blueprint for creating objects. 
# An object has properties and methods(functions) associated with it. 
# Almost everything in Python is an object, with its properties and methods. 
# A Class is like an object constructor, or a "blueprint" for creating objects.
#class will have properties and methods.
import datetime
from pydantic import BaseModel

class Employee:
    #The __init__ method is a special method that is automatically called 
    # when a new instance of the class is created.
    #Constructor method is used to initialize the attributes of the class.
    #self parameter is a reference to the current instance of the class 
    # and is used to access variables that belong to the class.
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    #The display_info method is used to display the information of the employee.
    #self parameter is a reference to the current instance of the class 
    # and is used to access variables that belong to the class.
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

    def calculate_bonus(self):
        bonus = (self.salary * 10) / 100  # Assuming a fixed bonus percentage of 10%
        print(f"Bonus for {self.name}: {bonus}")
        return bonus

#Creating an instance of the Employee class
employee1 = Employee("John Doe", 30, 50000) 
employee2 = Employee("Jane Smith", 25, 60000)
employee1.display_info()
employee2.display_info()
employee1.calculate_bonus()
employee2.calculate_bonus()

class Human:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def display_info(self):
        print(f"Name: {self.name}, Birth Year: {self.birth_year}")

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.birth_year
        print(f"{self.name} is {age} years old.")
        return age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.get_age()} years old.")    

#Creating an instance of the Human class
human1 = Human("Alice", 1985)
human2 = Human("Bob", 1988)
human1.display_info()
human2.display_info()
human1.get_age()
human2.get_age()
human1.introduce()
human2.introduce()

#pydantic module is another way to create classes with type hints and validation.
#pydantic class is used to create data models with validation and parsing capabilities.
#I want to create a data model for a user with name, age, and email fields 
# with type hints or type enforcement then pydantic class helps.

class User(BaseModel):
    name: str
    age: int
    email: str

#Creating an instance of the User class with valid data
user1 = User(name="Charlie", age=28, email="charlie@example.com")

print(user1)
print(user1.name)
print(user1.age)
print(user1.email)
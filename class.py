# 1. Create a Student class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# 2. Create objects from the Student class.
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)


# 3. Add attributes such as name and age.
print("Student 1 name:", student1.name)
print("Student 1 age:", student1.age)


# 4. Create a method that displays student information.
student1.display_info()
student2.display_info()


# 5. Use __init__() to initialize objects.
# __init__() is already used above to initialize name and age.


# 6. Create an Employee class with name and salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# 7. Create multiple objects from a class.
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

employee1.display_info()
employee2.display_info()


# 8. Create a BankAccount class with deposit and withdrawal methods.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account holder:", self.account_holder)
        print("Balance:", self.balance)


account = BankAccount("Alice", 10000)

account.deposit(2000)
account.withdraw(3000)
account.display_balance()


# 9. Create a Car class with start and stop methods.
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "started")

    def stop(self):
        print(self.brand, "stopped")


car = Car("Toyota")

car.start()
car.stop()


# 10. Create a Rectangle class that calculates area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())


# 11. Create a Student class that calculates average marks.
class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


student = StudentMarks("Alice", [80, 90, 85])

print("Student:", student.name)
print("Average marks:", student.average_marks())


# 12. Create class and instance variables.
class StudentDetails:

    # Class variable
    school = "ABC School"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age


student1 = StudentDetails("Alice", 20)
student2 = StudentDetails("Bob", 22)

print("School:", StudentDetails.school)
print("Student 1:", student1.name, student1.age)
print("Student 2:", student2.name, student2.age)


# 13. Create a class method.
class StudentCount:

    count = 0

    def __init__(self, name):
        self.name = name
        StudentCount.count += 1

    @classmethod
    def total_students(cls):
        return cls.count


student1 = StudentCount("Alice")
student2 = StudentCount("Bob")
student3 = StudentCount("Charlie")

print("Total students:", StudentCount.total_students())


# 14. Create a static method.
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("Addition:", Calculator.add(10, 20))
print("Multiplication:", Calculator.multiply(5, 4))
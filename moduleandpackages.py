# 1. Import and use the math module.

import math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Value of pi:", math.pi)
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))


# 2. Import only specific functions from a module.

from math import sqrt, factorial

print("Square root:", sqrt(36))
print("Factorial:", factorial(5))


# 3. Use the random module.

import random

print("Random number:", random.randint(1, 100))
print("Random decimal:", random.random())

numbers = [1, 2, 3, 4, 5]

print("Random choice:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled list:", numbers)


# 4. Use the datetime module.

from datetime import datetime, date

current_datetime = datetime.now()

print("Current date and time:", current_datetime)
print("Current date:", date.today())
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)

'''
# 5. Create your own Python module.

# Create a file named mymodule.py

# mymodule.py

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# 6. Import your custom module into another program.

# Create another file named main.py

# main.py

import mymodule

print("Addition:", mymodule.add(10, 20))
print("Multiplication:", mymodule.multiply(5, 4))

'''

# 7. Import specific functions from your custom module.

from mymodule import add, multiply

print("Addition:", add(10, 20))
print("Multiplication:", multiply(5, 4))


# 8. Create a package containing multiple modules.

# Folder structure:

# mypackage/
#     __init__.py
#     calculator.py
#     greetings.py


# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# greetings.py

def hello(name):
    return f"Hello, {name}"


# 9. Import a module from your package.

from mypackage import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))


# 10. Import a specific function from a package module.

from mypackage.greetings import hello

print(hello("Vaishnavi"))


# 11. Explore the os module.

import os

print("Current directory:", os.getcwd())
print("Files and folders:", os.listdir())


# 12. Explore the sys module.

import sys

print("Python version:", sys.version)
print("Python executable:", sys.executable)


# 13. Explore the statistics module.

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))


# 14. Explore the collections module.

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = Counter(numbers)

print("Frequency:", frequency)
print("Most common:", frequency.most_common(2))


# 15. Explore the json module.

import json

student = {
    "name": "Vaishnavi",
    "age": 21,
    "course": "AIML"
}

json_data = json.dumps(student)

print("JSON:", json_data)


# 16. Convert JSON data back into a Python dictionary.

python_data = json.loads(json_data)

print("Name:", python_data["name"])
print("Course:", python_data["course"])


# 17. Explore the time module.

import time

print("Current timestamp:", time.time())

print("Waiting for 2 seconds...")
time.sleep(2)

print("Done")


# 18. Explore the pathlib module.

from pathlib import Path

current_path = Path.cwd()

print("Current path:", current_path)
print("Directory contents:")

for item in current_path.iterdir():
    print(item)


# 19. Use aliases while importing modules.

import math as m

print("Square root:", m.sqrt(49))
print("Value of pi:", m.pi)


# 20. Check whether code is being run directly or imported.

def main():
    print("Program is running")


if __name__ == "__main__":
    main()
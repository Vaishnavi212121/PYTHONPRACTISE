# 1. Create a function that prints "Hello Python".
def print_hello():
    print("Hello Python")

print_hello()


# 2. Create a function that accepts two numbers and returns their sum.
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(10, 20))


# 3. Create a function to check whether a number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", check_even_odd(7))


# 4. Create a function to calculate factorial.
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print("Factorial:", factorial(5))


# 5. Create a function to calculate the area of a circle.
def circle_area(radius):
    return 3.14 * radius * radius

print("Area of circle:", circle_area(5))


# 6. Use positional arguments in a function.
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Vaishnavi", 21)


# 7. Use keyword arguments.
def employee_info(name, department, salary):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)

employee_info(
    name="Vaishnavi",
    department="AI/ML",
    salary=50000
)


# 8. Create a function with default arguments.
def greet(name="Python"):
    print("Hello", name)

greet()
greet("Vaishnavi")


# 9. Create a function using *args.
def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print("Sum:", calculate_sum(10, 20, 30, 40))

# 10. Create a function using **kwargs.
def display_details(**details):
    for key, value in details.items():
        print(key, ":", value)

display_details(
    name="Vaishnavi",
    age=21,
    skill="Python"
)

# 11. Create a function that returns multiple values.
def calculate_numbers(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

add, subtract, multiply = calculate_numbers(10, 5)

print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)

# 12. Create a function that accepts a list
# and returns its maximum value.
def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum

numbers = [10, 25, 7, 40, 15]

print("Maximum value:", find_maximum(numbers))

# 13. Create a function that counts vowels in a string.
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count

print("Number of vowels:", count_vowels("Hello Python"))


# 14. Create a function that removes duplicates from a list.
def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers

numbers = [1, 2, 3, 2, 4, 1, 5]

print("List without duplicates:", remove_duplicates(numbers))
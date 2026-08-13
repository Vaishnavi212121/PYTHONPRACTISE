# 1. Program to add, subtract, multiply, and divide two numbers
a = 10
b = 5
print("Addition:", a + b) # Returns 15
print("Subtraction:", a - b) # Returns 5
print("Multiplication:", a * b) # Returns 50
print("Division:", a / b) # Returns 2.0

# 2. Find the remainder when one number is divided by another using %
a = 10
b = 3
print("Remainder:",a % b) # Returns 1

# 3. Calculate the square and cube of a number using **
a = 4
print("Square:", a**2) # Returns 16
print("Cube:", a**3) # Returns 64

# 4. Check whether a number is even or odd using %
a = 7
if a % 2 == 0:
    print(a, "is even") 
else:
    print(a, "is odd")

# 5. Compare two numbers using >, <, >=, <=, ==, and !=
a = 10
b = 5
print("Is a greater than b?", a > b) # Returns True
print("Is a less than b?", a < b) # Returns False
print("Is a greater than or equal to b?", a >= b) # Returns True
print("Is a less than or equal to b?", a <= b) # Returns False
print("Is a equal to b?", a == b) # Returns False
print("Is a not equal to b?", a != b) # Returns True

# 6. Demonstrate the difference between / and //
a = 10
b = 3
print("Division using /:", a / b) # Returns a float
print("Division using //:", a // b) # Returns an integer 

# 7. Use +=, -=, *=, and /= on a variable
a = 10
a += 5
print("After += 5, a =", a) # Returns 15
a -= 3
print("After -= 3, a =", a) # Returns 12
a *= 2
print("After *= 2, a =", a) # Returns 24
a /= 4
print("After /= 4, a =", a) # Returns 6.0

# 8. Check whether a number is between 10 and 50 using comparison and logical operators
a = 25
if a > 10 and a < 50:
    print(a, "is between 10 and 50") # Returns True

# 9. Check whether a number is divisible by both 3 and 5.
a = 15
if a % 3 == 0 and a % 5 == 0:
    print(a, "is divisible by both 3 and 5") # Returns True

# 10. Use and, or, and not in condition
a = 10
b = 5
c = 15
if a > b and c > a:
    print("Both conditions are True")
if a > b or c < a:
    print("At least one condition is True")
if not (a < b):
    print("The condition is False")

# 11. Write a python program to find an average of two numbers entered by the user
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
average=(num1+num2)/2
print("The average is:", average)

# 12. Check the type of variable assigned using input() function
x = input("Enter a value: ")
print("The type of x is:", type(x))

# 13. Find the largest of three numbers using comparison operators.
a = 10
b = 20
c = 15
if a > b and a > c:
    print("The largest number is:", a)
elif b > c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

# 14. Check whether a person is eligible to vote using comparison operators.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 15. Check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 16. Calculate the total price after applying a discount.
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
total_price = price - (price * discount / 100)
print("The total price after discount is:", total_price)

# 17. Calculate simple interest using arithmetic operators.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)

# 18. Check whether a year is a leap year using logical operators.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 19. Check whether a number is divisible by 2 or 3 but not both.
num = int(input("Enter a number: "))
if (num % 2 == 0) != (num % 3 == 0):
    print(num, "is divisible by 2 or 3 but not both.")
else:
    print(num, "is not divisible by 2 or 3 but not both.")
'''
num = int(input("Enter a number: "))
# First check if it is a double-match
if num % 2 == 0 and num % 3 == 0:
    print(num, "is not divisible by 2 or 3 but not both.")
# If it's not a double-match, see if it matches at least one
elif num % 2 == 0 or num % 3 == 0:
    print(num, "is divisible by 2 or 3 but not both.")
else:
    print(num, "is not divisible by 2 or 3 but not both.")
      '''

# 20. Evaluate a complex expression containing +, -, *, /, %, //, and **.
expression = 2 + 3 * 4 - 5 / 2 % 3 // 2 ** 3
print("The result of the expression is:", expression)

# 21. Demonstrate operator precedence with a mathematical expression.
precedence_expression = 2 + 3 * 4
print("The result of the precedence expression is:", precedence_expression)

# 22. Use the in and not in operators with a list and string.
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list.")
if 6 not in my_list:
    print("6 is not in the list.")

my_string = "Hello, World!"
if "World" in my_string:
    print("'World' is in the string.")
if "Python" not in my_string:
    print("'Python' is not in the string.")

# 23. Write a program to determine whether three sides can form a triangle.
a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))
if a+b>c and b+c>a and c+a>b:
    print("The three sides can form a triangle.")
else:
    print("The three sides cannot form a triangle.")

# 24. Calculate a student's result using multiple comparison and logical operators.
marks=int(input("Enter the marks obtained :"))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# 25. Find the largest and smallest among five numbers without using max() or min().
#1Using Loop
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Start by assuming the first number is both the largest and smallest
largest = numbers[0]
smallest = numbers[0]
# Check each number in the list to update our largest and smallest values
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("The largest number is:", largest)
print("The smallest number is:", smallest)
'''
#2.Using sort:
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Sort the list from smallest to largest
numbers.sort()
# The first element is the smallest, the last is the largest
smallest = numbers[0]
largest = numbers[-1]
print("The largest number is:", largest)
print("The smallest number is:", smallest)
'''

# 26. Build a basic calculator using arithmetic and conditional operators.
# Take inputs from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on the operator
if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    # Prevent division by zero error
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operator!")

# 27. Write a program that checks whether a number is divisible by 2, 3, or 5 and displays the appropriate result.
num = int(input("Enter a number: "))

# Create a list to store what the number is divisible by
divisors = []

# Check each number individually
if num % 2 == 0:
    divisors.append("2")
if num % 3 == 0:
    divisors.append("3")
if num % 5 == 0:
    divisors.append("5")

# Display the appropriate result based on what we found
if len(divisors) == 0:
    print(f"{num} is not divisible by 2, 3, or 5.")
elif len(divisors) == 1:
    print(f"{num} is divisible by only {divisors[0]}.")
else:
    # Joins the numbers nicely with commas and 'and' (e.g., "2, 3 and 5")
    all_divisors = ", ".join(divisors[:-1]) + " and " + divisors[-1]
    print(f"{num} is divisible by {all_divisors}.")

# 1. Check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. Check whether a person is eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 4. Find the greater of two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is {num1}.")
else:
    print(f"The greater number is {num2}.")

# 5. Find the largest of three numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")

# 6. Create a grading system based on marks.
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# 7. Check whether a year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 8. Check whether a number is divisible by 3 and 5.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")

# 9. Check whether a person is eligible for a job based on age and qualification.
age = int(input("Enter your age: "))
qualification = input("Enter your qualification: ")
if age >= 18 and qualification.lower() == "bachelor":
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

# 10. Create a simple login system using username and password.
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password":
    print("Login successful.")
else:
    print("Invalid username or password.")
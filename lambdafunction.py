# 1. Create a lambda function to add two numbers.
add = lambda x, y: x + y
print("Sum using lambda:", add(5, 3))

# 2. Create a lambda function to square a number.
square = lambda x: x ** 2
print("Square using lambda:", square(5))

# 3. Use lambda to check whether a number is even.
is_even = lambda x: x % 2 == 0
print("Is 5 even?", is_even(5))
print("Is 6 even?", is_even(6))

# 4. Sort a list using a lambda function.
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(key=lambda x: x)
print("Sorted list:", numbers)

# 5. Sort a dictionary by its values using lambda.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
sorted_students = sorted(students.items(), key=lambda x: x[1])
print("Sorted students by marks:", sorted_students)

# 6. Use map() with lambda to square numbers.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# 7. Use filter() with lambda to find even numbers.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 8. Use reduce() with lambda to calculate a sum.
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers using reduce:", sum_of_numbers)

# 9. Sort student records by marks using lambda.
student_records = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_records = sorted(student_records, key=lambda x: x[1])
print("Sorted student records by marks:", sorted_records)

# 10. Find the highest-mark student using lambda.
highest_student = max(student_records, key=lambda x: x[1])
print("Student with highest marks:", highest_student)   
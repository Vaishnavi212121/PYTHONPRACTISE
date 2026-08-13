# 1. Create a tuple containing five numbers.
numbers = (1, 2, 3, 4, 5)
print("Tuple of numbers:", numbers)

# 2. Access the first and last elements.
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 3. Use positive and negative indexing.
print("Element at index 2:", numbers[2])
print("Element at index -2:", numbers[-2])

# 4. Slice a tuple.
print("First three elements:", numbers[:3])

# 5. Find the length of a tuple.
print("Length of the tuple:", len(numbers))

# 6. Check whether an element exists in a tuple.
if 5 in numbers:
    print("5 exists in the tuple")
else:
    print("5 does not exist in the tuple")

# 7. Count an element using count().
print("Count of 5:", numbers.count(5))

# 8. Find an element's position using index().
print("Index of 5:", numbers.index(5))

# 9. Loop through a tuple using for.
print("Elements in the tuple:")
for x in numbers:
    print(x)

# 10. Loop through a tuple using index numbers.
print("Elements in the tuple (with indices):")
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# 11. Loop through a tuple using while.
print("Elements in the tuple (with while loop):")
i = 0
while i < len(numbers):
    print(f"Index {i}: {numbers[i]}")
    i += 1

# 12. Convert a tuple into a list.
numbers_list = list(numbers)
print("Converted to list:", numbers_list)

# 13. Convert a list into a tuple.
numbers_tuple = tuple(numbers_list)
print("Converted to tuple:", numbers_tuple)

# 14. Join two tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print("Joined tuple:", joined_tuple)

# 15. Repeat a tuple using *.
repeated_tuple = numbers * 2
print("Repeated tuple:", repeated_tuple)

# 16. Unpack a tuple into separate variables.
a, b, c, d, e = numbers
print("Unpacked variables:", a, b, c, d, e)

# 17. Use * to collect multiple tuple values.
*first, last = numbers
print("First elements:", first)
print("Last element:", last)

# 18. Swap two variables using tuple unpacking.
x = 5
y = 10
x, y = y, x
print("Swapped variables:", x, y)

# 19. Find the largest and smallest value in a tuple.
print("Largest value:", max(numbers))
print("Smallest value:", min(numbers))

# 20. Find the sum of numeric values in a tuple.
print("Sum of numeric values:", sum(numbers))

# 21. Count how many times each element appears.
frequency = {}
for element in numbers:
    frequency[element] = frequency.get(element, 0) + 1
print("Frequency of each element:", frequency)
'''
for element in set(numbers):
    print(f"Count of {element}: {numbers.count(element)}")
'''

# 22. Remove an element from a tuple by converting it to a list.
numbers_list = list(numbers)
numbers_list.remove(5)
numbers = tuple(numbers_list)
print("Tuple after removing 5:", numbers)

# 23. Create a nested tuple and access its inner elements.
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("Inner element at index (1, 0):", nested_tuple[1][0])

# 24. Find common elements between two tuples.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common_elements = tuple(set(tuple1) & set(tuple2))#common_elements = tuple(x for x in tuple1 if x in tuple2)
print("Common elements:", common_elements)

# 25. Reverse a tuple.
reversed_tuple = numbers[::-1]
print("Reversed tuple:", reversed_tuple)

# 26. Remove duplicate elements from a tuple.
unique_tuple = tuple(set(numbers)) #unique_tuple = tuple(dict.fromkeys(numbers))
print("Tuple with duplicates removed:", unique_tuple)

# 27. Find the second-largest value in a tuple.
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers) >= 2:
    print("Second-largest value:", unique_numbers[1])
else:
    print("No second-largest value")

# 28. Find the frequency of each element in a tuple.
frequency = {}
for element in numbers:
    frequency[element] = frequency.get(element, 0) + 1
print("Frequency of each element:", frequency)

# 29. Convert a nested tuple into a flat tuple.
flat_tuple = tuple(item for sublist in nested_tuple for item in sublist)
print("Flat tuple:", flat_tuple)

# 30. Sort a tuple without directly modifying it.
sorted_tuple = tuple(sorted(numbers))
print("Sorted tuple:", sorted_tuple)

# 31. Find all pairs in a tuple whose sum equals a target.
target = 10
pairs = [(numbers[i], numbers[j]) for i in range(len(numbers)) for j in range(i+1, len(numbers)) if numbers[i] + numbers[j] == target]
print("Pairs whose sum equals", target, ":", pairs)

# 32. Check whether two tuples contain the same elements.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (5, 4, 3, 2, 1)
print("Tuples contain the same elements:", set(tuple1) == set(tuple2))

# 33. Convert a tuple of key-value pairs into a dictionary.
key_value_pairs = (('a', 1), ('b', 2), ('c', 3))
dictionary = dict(key_value_pairs)
print("Dictionary:", dictionary)

# 34. Create a tuple containing student records and find the student with the highest marks.
student_records = (('Alice', 85), ('Bob', 90), ('Charlie', 78))
highest_student = max(student_records, key=lambda x: x[1])
print("Student with highest marks:", highest_student)

# 35. Sort a tuple of student records based on marks.
sorted_students = tuple(sorted(student_records, key=lambda x: x[1], reverse=True))
print("Sorted student records:", sorted_students)
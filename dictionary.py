# 1. Create a dictionary containing student name, age, and marks.
student = {"name": "Alice", "age": 20, "marks": 85}
print("Student dictionary:", student)

# 2. Access a value using its key.
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student marks:", student["marks"])

# 3. Add a new key-value pair.
student["grade"] = "A"
print("Dictionary after adding grade:", student)

# 4. Update an existing value.
student["marks"] = 90
print("Dictionary after updating marks:", student)

# 5. Remove an item using pop().
removed_value = student.pop("age")
print("Dictionary after removing age:", student)
print("Removed value:", removed_value)

# 6. Remove the last inserted item using popitem().
last_item = student.popitem()
print("Dictionary after removing last item:", student)
print("Last item:", last_item)

# 7. Check whether a key exists using in.
if "name" in student:
    print("Key 'name' exists in the dictionary")

# 8. Find the number of items using len().
print("Number of items in the dictionary:", len(student))

# 9. Print all keys using keys().
print("All keys:", list(student.keys()))

# 10. Print all values using values().
print("All values:", list(student.values()))

# 11. Print all key-value pairs using items().
print("All key-value pairs:", list(student.items()))
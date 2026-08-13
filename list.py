# 1. Create a list of five numbers and print it.
numbers = [1, 2, 3, 4, 5]
print("List of numbers:", numbers)

# 2. Access the first, last, and middle elements.
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Middle element:", numbers[len(numbers)//2])

'''
for middle no :
numbers = [1, 2, 3, 4, 5, 6]
n = len(numbers)
if n % 2 == 1:
    middle = numbers[n // 2]
    print("Middle element:", middle)
else:
    middle1 = numbers[n // 2 - 1]
    middle2 = numbers[n // 2]
    print("Middle elements:", middle1, middle2)
    '''

# 3. Access list elements using positive and negative indexing.
numbers = [1, 2, 3, 4, 5]
print("Element at index 2:", numbers[2]) #positive indexing starts from 0
print("Element at index -2:", numbers[-2]) #negative indexing starts from -1

# 4. Slice a list to get the first three elements.
numbers = [1, 2, 3, 4, 5]
print("First three elements:", numbers[:3])

# 5. Reverse a list using slicing.
numbers = [1, 2, 3, 4, 5]
print("Reversed list:", numbers[::-1])

# 6. Add an item using append().
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("List after appending 6:", numbers)

# 7. Add multiple items using extend().
numbers = [1, 2, 3, 4, 5]
numbers.extend([7, 8, 9])
print("List after extending:", numbers)

# 8. Insert an item at a specific position using insert().
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 10)
print("List after inserting 10 at index 2:", numbers)

# 9. Remove an item using remove().
numbers = [1, 2, 3, 4, 5]
numbers.remove(10)
print("List after removing 10:", numbers)

# 10. Remove the last item using pop().
numbers = [1, 2, 3, 4, 5]
numbers.pop()
print("List after popping the last item:", numbers)

# 11. Delete an item using del.
del numbers[0]
print("List after deleting the first item:", numbers)

# 12. Empty a list using clear().
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print("List after clearing:", numbers)

# 13. Check whether an item exists using in.
numbers = [1, 2, 3, 4, 5]
if 5 in numbers:
    print("5 exists in the list")
else:
    print("5 does not exist in the list")

# 14. Find the length of a list.
numbers = [1, 2, 3, 4, 5]
print("Length of the list:", len(numbers))

# 15. Sort a list in ascending and descending order.
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print("List sorted in ascending order:", numbers)
numbers.sort(reverse=True)
print("List sorted in descending order:", numbers)

# 16. Find the largest and smallest number in a list.
numbers = [5, 2, 8, 1, 9]
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

# 17. Find the sum of all numbers in a list.
numbers = [5, 2, 8, 1, 9]
print("Sum of all numbers:", sum(numbers))

# 18. Count how many times an element occurs.
numbers = [5, 2, 8, 1, 9, 2, 5]
print("Count of 5:", numbers.count(5))

# 19. Find the index of a particular element.
numbers = [5, 2, 8, 1, 9]
print("Index of 8:", numbers.index(8))

# 20. Remove duplicate elements from a list.
'''#the order may change.
numbers = [5, 2, 8, 1, 9, 2, 5]
unique_numbers = list(set(numbers))
print("List with duplicates removed:", unique_numbers)
'''
numbers = [5, 2, 8, 1, 9, 2, 5]
unique_numbers = []
for x in numbers:
    if x not in unique_numbers:
        unique_numbers.append(x)
print("List with duplicates removed:", unique_numbers)

# 21. Separate even and odd numbers into two lists.
numbers = [5, 2, 8, 1, 9]
even_numbers = [x for x in numbers if x % 2 ==0]
odd_numbers = [x for x in numbers if x % 2 !=0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# 22. Find the second-largest number in a list.
'''#works when all numbers are different:
numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print("Second-largest number:", numbers[1])
'''
numbers = [5, 2, 8, 1, 9]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers) >= 2:
    print("Second-largest number:", unique_numbers[1])
else:
    print("No second-largest number")

# 23. Find the second-smallest number in a list.
'''#works when all numbers are different:
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print("Second-smallest number:", numbers[1])
'''
numbers = [5, 2, 8, 1, 9]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    print("Second-smallest number:", unique_numbers[1])
else:
    print("No second-smallest number")

# 24. Reverse a list without using reverse().
numbers = [5, 2, 8, 1, 9]
reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)

# 25. Copy one list into another.
numbers = [5, 2, 8, 1, 9]
new_numbers = numbers.copy()
print("Copied list:", new_numbers)

# 26. Merge two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list:", merged_list)

# 27. Find common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [x for x in list1 if x in list2]
print("Common elements:", common_elements)

# 28. Find elements present in one list but not another.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
elements_only_in_list1 = [x for x in list1 if x not in list2]
print("Elements only in list1:", elements_only_in_list1)

# 29. Create a list of squares from 1 to 20.
squares = [x**2 for x in range(1, 21)]
print("Squares from 1 to 20:", squares)

# 30. Convert a list of strings into uppercase strings.
strings = ["hello", "world", "python"]
uppercase_strings = [s.upper() for s in strings]
print("Uppercase strings:", uppercase_strings)

# 31. Find the frequency of every element in a list.
numbers = [5, 2, 8, 1, 9, 2, 5]
frequency = {x: numbers.count(x) for x in set(numbers)}
print("Frequency of each element:", frequency)
'''#using loop:
numbers = [5, 2, 8, 1, 9, 2, 5]
frequency = {}
for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1
print("Frequency of each element:", frequency)'''

# 32. Find the most frequently occurring element.
numbers = [5, 2, 8, 1, 9, 2, 5]
frequency = {}
for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1
most_frequent = max(frequency, key=frequency.get)
print("Most frequently occurring element:", most_frequent)

# 33. Rotate a list to the left by k positions.
numbers = [1, 2, 3, 4, 5]
k = 7
k = k % len(numbers)
rotated_left = numbers[k:] + numbers[:k]
print("List rotated left by", k, "positions:", rotated_left)

# 34. Rotate a list to the right by k positions.
numbers = [1, 2, 3, 4, 5]
k = 7
k = k % len(numbers)
rotated_right = numbers[-k:] + numbers[:-k]
print("List rotated right by", k, "positions:", rotated_right)

# 35. Find all pairs whose sum equals a given number.
numbers = [1, 2, 3, 4, 5]
target = 6
pairs = [(x, y) for x in numbers for y in numbers if x + y == target and x < y]
print("Pairs whose sum equals", target, ":", pairs)
'''
numbers = [1, 2, 3, 4, 5]
target = 6
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
print("Pairs whose sum equals", target, ":", pairs)
'''

# 36. Find the intersection of three lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]
intersection = [x for x in list1 if x in list2 and x in list3]
print("Intersection of three lists:", intersection)

# 37. Flatten a nested list.
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)

# 38. Find the missing number from a list containing numbers from 1 to N.
numbers = [1, 2, 4, 5]
n = len(numbers) + 1
missing_number = n * (n + 1) // 2 - sum(numbers)
print("Missing number:", missing_number)

# 39. Find duplicate numbers in a list.
numbers = [1, 2, 3, 2, 4, 5, 4]
duplicates = [x for x in set(numbers) if numbers.count(x) > 1]
print("Duplicate numbers:", duplicates)

# 40. Move all zeros to the end of a list.
numbers = [0, 1, 0, 3, 12]
numbers = [x for x in numbers if x != 0] + [0] * numbers.count(0)
print("List with zeros at the end:", numbers)

# 41. Find the longest increasing sequence in a list.
numbers = [10, 9, 2, 5, 7, 1]
longest = []
current = []
for i in range(len(numbers)):

    if i == 0 or numbers[i] > numbers[i - 1]:
        current.append(numbers[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [numbers[i]]
if len(current) > len(longest):
    longest = current
print("Longest increasing sequence:", longest)
print("Length:", len(longest))

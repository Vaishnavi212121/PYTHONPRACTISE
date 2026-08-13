# 1. Create a set containing five elements.
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

# 2. Add an element using add().
my_set.add(6)
print("Set after adding 6:", my_set)

# 3. Add multiple elements using update().
my_set.update([7, 8, 9])
print("Set after updating with [7, 8, 9]:", my_set)

# 4. Remove an element using remove().
my_set.remove(5)
print("Set after removing 5:", my_set)

# 5. Remove an element using discard().
my_set.discard(10)  # This will not raise an error if the element is not present
print("Set after discarding 10:", my_set)

# 6. Demonstrate the difference between remove() and discard().
try:
    my_set.remove(10)  # This will raise a KeyError if the element is not present
except KeyError:
    print("Element not found in the set.")

my_set.discard(10)  # This will not raise an error if the element is not present
print("Set after discarding 10:", my_set)

# 7. Remove an arbitrary element using pop().
arbitrary_element = my_set.pop()
print("Set after popping an arbitrary element:", my_set)
print("Popped element:", arbitrary_element)

# 8. Empty a set using clear().
my_set.clear()
print("Set after clearing:", my_set)

# 9. Check whether an element exists using in.
if 5 in my_set:
    print("5 exists in the set")
else:
    print("5 does not exist in the set")

# 10. Find the number of elements using len().
print("Number of elements in the set:", len(my_set))

# 11. Find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)

# 12. Find the intersection of two sets.
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# 13. Find the difference between two sets.
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)

# 14. Find the symmetric difference between two sets.
symmetric_diff_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", symmetric_diff_set)

# 15. Use union() and |.
union_set = set1 | set2
print("Union using |:", union_set)

# 16. Use intersection() and &.
intersection_set = set1 & set2
print("Intersection using &:", intersection_set)

# 17. Use difference() and -.
difference_set = set1 - set2
print("Difference using -:", difference_set)

# 18. Use symmetric_difference() and ^.
symmetric_diff_set = set1 ^ set2
print("Symmetric difference using ^:", symmetric_diff_set)

# 19. Check whether one set is a subset of another.
if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")

# 20. Check whether one set is a superset of another.
if set1.issuperset(set2):
    print("Set1 is a superset of Set2")
else:
    print("Set1 is not a superset of Set2")

# 21. Check whether two sets are disjoint.
if set1.isdisjoint(set2):
    print("Set1 and Set2 are disjoint")
else:
    print("Set1 and Set2 are not disjoint")

# 22. Find common students between two classes.
class_a_students = {"Alice", "Bob", "Charlie", "David"}
class_b_students = {"Charlie", "David", "Eve", "Frank"}
common_students = class_a_students.intersection(class_b_students)
print("Common students:", common_students)

# 23. Find students who are in Class A but not Class B.
only_class_a_students = class_a_students.difference(class_b_students)
print("Students in Class A but not in Class B:", only_class_a_students)

# 24. Find students who are in either class but not both.
either_class_students = class_a_students.symmetric_difference(class_b_students)
print("Students in either class but not both:", either_class_students)

# 25. Remove duplicate values from a list using a set.
original_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_list = list(set(original_list))
print("List with duplicates removed:", unique_list)
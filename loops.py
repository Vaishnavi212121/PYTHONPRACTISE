# 1. Print numbers from 1 to 10 using for.
for i in range(1, 11):
    print(i)

# 2. Print numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)

# 3. Print all even numbers from 1 to 100.
for i in range(2, 101, 2):
    print(i)

# 4. Print all odd numbers from 1 to 100.
for i in range(1, 101, 2):
    print(i)

# 5. Calculate the sum of numbers from 1 to 100.
total = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)

# 6. Print the multiplication table of a number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7. Use a while loop to print numbers from 1 to 10.
i = 1
while i <= 10:
    print(i)
    i += 1
# 1. Create a string and print it.
string1 = "This is new string"
print(string1)

# 2. Find the length of a string using len().
print("Length of string",len(string1))

# 3. Access the first and last character of a string.
print("First character:", string1[0])
print("Last character:", string1[-1])

# 4. Access characters using positive and negative indexing.
print("Character at index 5:", string1[5])
print("Character at index -5:", string1[-5])

# 5. Print the first five characters using slicing.
print("First five characters:", string1[:5])

# 6. Reverse a string using slicing.
print("Reversed string:", string1[::-1])

# 7. Convert a string to uppercase and lowercase.
print("Uppercase:", string1.upper())
print("Lowercase:", string1.lower())

# 8. Remove spaces from the beginning and end using strip().
string2 = "   This is a string with spaces   "
print("String with spaces:", string2)
print("String without spaces:", string2.strip())

# 9. Replace one word with another using replace().
print("String after replacement:", string1.replace("new", "old"))

# 10. Count how many times a character appears using count().
print("Count of 's' in string:", string1.count("s"))

# 11. Check whether a word exists inside a string using in.
if "new" in string1:
    print("'new' exists in the string")

# 12. Find the position of a substring using find().
print("Position of 'new' in string:", string1.find("new"))

# 13. Split a sentence into a list of words.
sentence = "This is a sentence"
words = sentence.split()
print("List of words:", words)

# 14. Join a list of words into a string.
print("Joined string:", " ".join(words))

# 15. Check whether a string starts or ends with a particular word.
print("String starts with 'This':", string1.startswith("This"))
print("String ends with 'string':", string1.endswith("string"))

# 16. Count the number of vowels in a string.
vowels = "aeiou"
vowel_count = sum(1 for char in string1.lower() if char in vowels)
print("Number of vowels in string:", vowel_count)

# 17. Count vowels, consonants, digits, and spaces separately.
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
digits = "0123456789"
spaces = " "
#generator expression hands over the numbers one by one to the sum()
vowel_count = sum(1 for char in string1.lower() if char in vowels)
consonant_count = sum(1 for char in string1.lower() if char in consonants)
digit_count = sum(1 for char in string1 if char in digits)
space_count = sum(1 for char in string1 if char in spaces)

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Number of digits:", digit_count)
print("Number of spaces:", space_count)

# 18. Reverse each word in a sentence.
words_reversed = [word[::-1] for word in words] #List Comprehension
print("Sentence with reversed words:", " ".join(words_reversed))

# 19. Find the longest word in a sentence.
longest_word = max(words, key=len)
print("Longest word:", longest_word)
'''
The max() function scans your list
and uses key=len to measure the length of
each individual word. Instead of looking at alphabetical order,
it picks out the word with the most characters and saves it to your variable.
'''

# 20. Find the shortest word in a sentence.
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)

# 21. Check whether a string contains only digits using isdigit().
print("Contains only digits:", string1.isdigit())

# 22. Check whether a string contains only alphabetic characters using isalpha().
print("Contains only alphabetic characters:", string1.isalpha())

# 23. Convert "hello world python" into "Hello World Python".
sentence2 = "hello world python"
print("Converted sentence:", sentence2.title()) # sentence2.capitalize() also can be used 
'''title() searches your sentence for spaces
 and turns the very next character into a capital letter.'''

# 24. Find the first non-repeated character in a string1.
s = "swiss"
for char in s:
    if s.count(char) == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found")

# 25. Find all duplicate characters in a string.
duplicates = set()
for char in s:
    if s.count(char) > 1:
        duplicates.add(char)
print("Duplicate characters:", duplicates)

# 26. Count the frequency of every character.
char_freq = {}
for char in s:
    char_freq[char] = char_freq.get(char, 0) + 1
print("Character frequencies:", char_freq)

# 27. Check whether two strings are anagrams.
str1 = "listen"
str2 = "silent"
print("Are anagrams:", sorted(str1.lower()) == sorted(str2.lower()))

# 28. Remove duplicate characters while preserving their order.
unique_chars = []
for char in s:
    if char not in unique_chars:
        unique_chars.append(char)
print("String without duplicates:", ''.join(unique_chars))

# 29. Find the most frequently occurring character.
most_frequent = max(char_freq, key=char_freq.get)
print("Most frequent character:", most_frequent)

# 30. Find the second most frequently occurring character.
second_most_frequent = sorted(char_freq, key=char_freq.get, reverse=True)[1]
print("Second most frequent character:", second_most_frequent)

# 31. Compress a string using character counts. Example: aaabbc → a3b2c1
s = "aaabbc"
result = ""
count = 1
for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
print(result)

# 32. Find the longest substring without repeating characters.
s = "abcabcbb"
longest = ""
for i in range(len(s)):
    current = ""
    for j in range(i, len(s)):
        if s[j] in current:
            break
        current += s[j]
    if len(current) > len(longest):
        longest = current
print("Longest substring:", longest)
print("Length:", len(longest))

# 33. Create a password validator using string methods and logical operators.
def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        return "Password must contain at least one special character."
    return "Password is valid."


# =========================================================
# Example 21 - Find Text (find())
# =========================================================

# find() returns the index position of a word.
# If the word is not found, it returns -1.

text = "Python Programming"

print("Example 21")

position = text.find("Programming")

print(position)

print("\n" + "=" * 50)


# =========================================================
# Example 22 - Index Method (index())
# =========================================================

# index() works like find().
# But if the word does not exist,
# it gives an error.

text = "Python Programming"

print("Example 22")

position = text.index("Python")

print(position)

print("\n" + "=" * 50)


# =========================================================
# Example 23 - Count Characters (count())
# =========================================================

# count() counts how many times
# a character or word appears.

text = "banana"

print("Example 23")

print(text.count("a"))
print(text.count("n"))

print("\n" + "=" * 50)


# =========================================================
# Example 24 - Starts With (startswith())
# =========================================================

# Checks whether a string starts
# with a specific value.

text = "Python Programming"

print("Example 24")

print(text.startswith("Python"))
print(text.startswith("Java"))

print("\n" + "=" * 50)


# =========================================================
# Example 25 - Ends With (endswith())
# =========================================================

# Checks whether a string ends
# with a specific value.

filename = "document.pdf"

print("Example 25")

print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

print("\n" + "=" * 50)


# =========================================================
# Example 26 - Split String (split())
# =========================================================

# split() converts a string into a list.

text = "Apple,Banana,Mango"

print("Example 26")

fruits = text.split(",")

print(fruits)

print("\n" + "=" * 50)


# =========================================================
# Example 27 - Split Sentence into Words
# =========================================================

sentence = "Python is easy to learn"

print("Example 27")

words = sentence.split()

print(words)

print("\n" + "=" * 50)


# =========================================================
# Example 28 - Join Strings (join())
# =========================================================

# join() combines list items into one string.

names = ["John", "David", "Alex"]

print("Example 28")

result = ", ".join(names)

print(result)

print("\n" + "=" * 50)


# =========================================================
# Example 29 - Check Alphabet (isalpha())
# =========================================================

# Returns True if all characters are letters.

text1 = "Python"
text2 = "Python123"

print("Example 29")

print(text1.isalpha())
print(text2.isalpha())

print("\n" + "=" * 50)


# =========================================================
# Example 30 - Check Digits (isdigit())
# =========================================================

# Returns True if all characters are numbers.

number1 = "12345"
number2 = "123abc"

print("Example 30")

print(number1.isdigit())
print(number2.isdigit())

print("\n" + "=" * 50)


# =========================================================
# Example 31 - Check Letters and Numbers (isalnum())
# =========================================================

# alphanumeric means:
# letters + numbers

value1 = "Python123"
value2 = "Python@123"

print("Example 31")

print(value1.isalnum())
print(value2.isalnum())

print("\n" + "=" * 50)


# =========================================================
# Example 32 - Check Spaces (isspace())
# =========================================================

text1 = "     "
text2 = "Python"

print("Example 32")

print(text1.isspace())
print(text2.isspace())

print("\n" + "=" * 50)


# =========================================================
# Example 33 - Check Lowercase (islower())
# =========================================================

text = "python"

print("Example 33")

print(text.islower())

print("\n" + "=" * 50)


# =========================================================
# Example 34 - Check Uppercase (isupper())
# =========================================================

text = "PYTHON"

print("Example 34")

print(text.isupper())

print("\n" + "=" * 50)


# =========================================================
# Example 35 - String Formatting Using f-string
# =========================================================

# f-string allows inserting variables
# directly inside a string.

name = "Kamal"
age = 21

print("Example 35")

print(f"My name is {name}")
print(f"I am {age} years old")

print("\n" + "=" * 50)


# =========================================================
# Example 36 - format() Method
# =========================================================

name = "Nimal"
marks = 85

print("Example 36")

message = "Student: {} | Marks: {}".format(name, marks)

print(message)

print("\n" + "=" * 50)


# =========================================================
# Example 37 - Loop Through a String
# =========================================================

# Strings are iterable.
# We can access each character using a loop.

word = "Python"

print("Example 37")

for letter in word:
    print(letter)

print("\n" + "=" * 50)


# =========================================================
# Example 38 - Count Vowels in a String
# =========================================================

text = "Programming"

count = 0

for letter in text.lower():

    if letter in "aeiou":
        count += 1

print("Example 38")

print("Number of vowels:", count)

print("\n" + "=" * 50)


# =========================================================
# Example 39 - Reverse String Using Loop
# =========================================================

text = "Python"

reverse = ""

for letter in text:
    reverse = letter + reverse

print("Example 39")

print(reverse)

print("\n" + "=" * 50)


# =========================================================
# Example 40 - Palindrome Checking
# =========================================================

# A palindrome is a word that is same
# forward and backward.
#
# Example:
# madam
# level

word = "madam"

print("Example 40")

if word == word[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")

print("\n" + "=" * 50)


# =========================================================
# Example 41 - Remove All Spaces
# =========================================================

text = "Python Programming Language"

print("Example 41")

new_text = text.replace(" ", "")

print(new_text)

print("\n" + "=" * 50)


# =========================================================
# Example 42 - Count Words in Sentence
# =========================================================

sentence = "Python is easy and powerful"

print("Example 42")

words = sentence.split()

print("Number of words:", len(words))

print("\n" + "=" * 50)


# =========================================================
# Example 43 - User Input String Example
# =========================================================

# input() always returns a string.

name = input("Enter your name: ")

print("Example 43")

print("Hello", name)

print("\n" + "=" * 50)


# =========================================================
# Example 44 - Simple Username Checker
# =========================================================

username = input("Enter username: ")

print("Example 44")

if username.isalnum():
    print("Valid username")

else:
    print("Username should contain only letters and numbers")


print("\n" + "=" * 50)


# =========================================================
# Example 45 - String Comparison
# =========================================================

# Strings can be compared using ==

password = "python123"

print("Example 45")

if password == "python123":
    print("Correct password")

else:
    print("Wrong password")


print("\n=========================================================")
print("End of Python String Notes - Part 2")
print("=========================================================")


"""
=========================================================
                  STRING QUICK SUMMARY
=========================================================

len()
    -> Find string length

upper()
    -> Convert to uppercase

lower()
    -> Convert to lowercase

strip()
    -> Remove spaces

replace()
    -> Replace text

find()
    -> Find position

count()
    -> Count characters

split()
    -> Convert string to list

join()
    -> Convert list to string

isalpha()
    -> Check letters

isdigit()
    -> Check numbers

isalnum()
    -> Check letters + numbers

startswith()
    -> Check beginning

endswith()
    -> Check ending

f-string
    -> Easy string formatting


Important:
-----------
Strings are immutable.
This means the original string
cannot be changed directly.

Example:

text = "Python"

text[0] = "J"   ❌ Error

Create a new string instead.

=========================================================
"""
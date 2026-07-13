"""
=========================================================
              PYTHON STRINGS NOTES
=========================================================

What is a String?
-----------------
A string is a collection of characters used to store text.

Examples:
    "Hello"
    'Python'
    "12345"

Strings can contain:
    - Letters
    - Numbers
    - Symbols
    - Spaces

String data type:
    str

=========================================================
"""


# =========================================================
# Example 1 - Creating Strings
# =========================================================

# Strings can be created using single quotes
name = 'John'

# Strings can also be created using double quotes
city = "Colombo"

print("Example 1")
print(name)
print(city)

print("\n" + "=" * 50)


# =========================================================
# Example 2 - Checking String Data Type
# =========================================================

# type() shows the data type of a variable

text = "Python"

print("Example 2")
print(type(text))

# Output:
# <class 'str'>

print("\n" + "=" * 50)


# =========================================================
# Example 3 - Multi-line Strings
# =========================================================

# Triple quotes allow writing strings
# across multiple lines.

message = """
Welcome to Python.
This is a multiline string example.
"""

print("Example 3")
print(message)

print("\n" + "=" * 50)


# =========================================================
# Example 4 - String Length (len())
# =========================================================

# len() counts the number of characters
# inside a string.

word = "Python"

length = len(word)

print("Example 4")
print("Length =", length)

# Output:
# Length = 6

print("\n" + "=" * 50)


# =========================================================
# Example 5 - String Indexing
# =========================================================

# Each character has an index number.
#
# Python indexing starts from 0.
#
# P  y  t  h  o  n
# 0  1  2  3  4  5

language = "Python"

print("Example 5")

print(language[0])
print(language[2])
print(language[5])

print("\n" + "=" * 50)


# =========================================================
# Example 6 - Negative Indexing
# =========================================================

# Negative indexes start from the end.
#
# P   y   t   h   o   n
# -6 -5  -4  -3  -2  -1

word = "Python"

print("Example 6")

print(word[-1])
print(word[-2])
print(word[-6])

print("\n" + "=" * 50)


# =========================================================
# Example 7 - String Slicing
# =========================================================

# Slicing extracts a part of a string.
#
# Syntax:
# string[start:end]
#
# The end index is NOT included.

text = "Programming"

print("Example 7")

print(text[0:7])
print(text[3:8])

print("\n" + "=" * 50)


# =========================================================
# Example 8 - Slicing Without Start or End
# =========================================================

word = "Python"

print("Example 8")

# Start from beginning
print(word[:3])

# Go until the end
print(word[3:])

print("\n" + "=" * 50)


# =========================================================
# Example 9 - Reverse a String
# =========================================================

# [::-1] reverses a string.

text = "Python"

reverse = text[::-1]

print("Example 9")

print(reverse)

print("\n" + "=" * 50)


# =========================================================
# Example 10 - String Concatenation
# =========================================================

# + operator joins strings together.

first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name

print("Example 10")

print(full_name)

print("\n" + "=" * 50)


# =========================================================
# Example 11 - String Repetition
# =========================================================

# * repeats a string multiple times.

text = "Hello "

print("Example 11")

print(text * 3)

print("\n" + "=" * 50)


# =========================================================
# Example 12 - Membership Operators
# =========================================================

# "in" checks whether a word exists inside a string.

sentence = "Python Programming"

print("Example 12")

print("Python" in sentence)
print("Java" in sentence)

print("\n" + "=" * 50)


# =========================================================
# Example 13 - Escape Characters
# =========================================================

print("Example 13")

# New line
print("Hello\nWorld")

# Tab space
print("Name\tAge")

# Double quote inside string
print("He said \"Python is easy\"")

# Backslash
print("C:\\Users\\Student")

print("\n" + "=" * 50)


# =========================================================
# Example 14 - Convert String to Uppercase
# =========================================================

text = "python"

print("Example 14")

print(text.upper())

print("\n" + "=" * 50)


# =========================================================
# Example 15 - Convert String to Lowercase
# =========================================================

text = "PYTHON"

print("Example 15")

print(text.lower())

print("\n" + "=" * 50)


# =========================================================
# Example 16 - Capitalize String
# =========================================================

text = "python programming"

print("Example 16")

print(text.capitalize())

print("\n" + "=" * 50)


# =========================================================
# Example 17 - Title Case
# =========================================================

text = "python programming language"

print("Example 17")

print(text.title())

print("\n" + "=" * 50)


# =========================================================
# Example 18 - Swap Case
# =========================================================

text = "PyThOn"

print("Example 18")

print(text.swapcase())

print("\n" + "=" * 50)


# =========================================================
# Example 19 - Remove Spaces
# =========================================================

text = "   Python   "

print("Example 19")

print(text.strip())

print("\n" + "=" * 50)


# =========================================================
# Example 20 - Replace Text
# =========================================================

text = "I like Java"

print("Example 20")

new_text = text.replace("Java", "Python")

print(new_text)


print("\n=========================================================")
print("End of Python String Notes - Part 1")
print("=========================================================")
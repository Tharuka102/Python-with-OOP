# Python Strings Notes

## What is a String?

A **string** is a sequence of characters used to store text.

Strings can contain:
- Letters
- Numbers
- Symbols
- Spaces

In Python, strings are written inside quotation marks.

```python
name = "John"
city = 'Colombo'

print(name)
print(city)
```

**Output**

```
John
Colombo
```

---

# Creating Strings

You can create strings using **single quotes** or **double quotes**.

```python
text1 = 'Hello'
text2 = "Python"

print(text1)
print(text2)
```

---

# Triple Quotes (Multi-line Strings)

Triple quotes allow strings to span multiple lines.

```python
message = """
Welcome to Python.
This is a multi-line string.
"""

print(message)
```

**Output**

```
Welcome to Python.
This is a multi-line string.
```

---

# String Data Type

Use `type()` to check the data type.

```python
name = "Alice"

print(type(name))
```

**Output**

```
<class 'str'>
```

---

# String Length

Use `len()` to count characters.

```python
text = "Python"

print(len(text))
```

**Output**

```
6
```

---

# String Indexing

Each character has an index.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

```python
word = "Python"

print(word[0])
print(word[3])
print(word[5])
```

**Output**

```
P
h
n
```

---

# Negative Indexing

Negative indexes count from the end.

```
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

```python
word = "Python"

print(word[-1])
print(word[-2])
```

**Output**

```
n
o
```

---

# String Slicing

Syntax

```python
string[start:end]
```

The end index is **not included**.

```python
text = "Python"

print(text[0:3])
print(text[2:6])
```

**Output**

```
Pyt
thon
```

---

# Skip Characters

```python
text = "Python"

print(text[::2])
```

**Output**

```
Pto
```

---

# Reverse a String

```python
text = "Python"

print(text[::-1])
```

**Output**

```
nohtyP
```

---

# String Concatenation

Join strings using `+`.

```python
first = "Hello"
second = "World"

result = first + " " + second

print(result)
```

**Output**

```
Hello World
```

---

# String Repetition

Use `*`.

```python
print("Hi " * 3)
```

**Output**

```
Hi Hi Hi
```

---

# Membership Operators

Check whether text exists.

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
```

**Output**

```
True
False
```

---

# Escape Characters

## New Line

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

## Tab

```python
print("Name\tAge")
```

Output

```
Name    Age
```

---

## Double Quote

```python
print("He said \"Hello\"")
```

Output

```
He said "Hello"
```

---

## Backslash

```python
print("C:\\Users\\John")
```

Output

```
C:\Users\John
```

---

# Convert to Uppercase

```python
text = "python"

print(text.upper())
```

Output

```
PYTHON
```

---

# Convert to Lowercase

```python
text = "PYTHON"

print(text.lower())
```

Output

```
python
```

---

# Capitalize

```python
text = "python programming"

print(text.capitalize())
```

Output

```
Python programming
```

---

# Title Case

```python
text = "python programming"

print(text.title())
```

Output

```
Python Programming
```

---

# Swap Case

```python
text = "PyThOn"

print(text.swapcase())
```

Output

```
pYtHoN
```

---

# Remove Spaces

```python
text = "   Python   "

print(text.strip())
```

Output

```
Python
```

---

# Remove Left Spaces

```python
text = "   Python"

print(text.lstrip())
```

---

# Remove Right Spaces

```python
text = "Python    "

print(text.rstrip())
```

---

# Replace Text

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output

```
I like Python
```

---

# Find Text

```python
text = "Python Programming"

print(text.find("Program"))
```

Output

```
7
```

---

# Count Characters

```python
text = "banana"

print(text.count("a"))
```

Output

```
3
```

---

# Starts With

```python
text = "Python"

print(text.startswith("Py"))
```

Output

```
True
```

---

# Ends With

```python
text = "Python"

print(text.endswith("on"))
```

Output

```
True
```

---

# Split String

```python
text = "Apple,Banana,Mango"

print(text.split(","))
```

Output

```
['Apple', 'Banana', 'Mango']
```

---

# Join Strings

```python
items = ["Apple", "Banana", "Orange"]

print(", ".join(items))
```

Output

```
Apple, Banana, Orange
```

---

# Check Alphabet

```python
print("Python".isalpha())
```

Output

```
True
```

---

# Check Digits

```python
print("12345".isdigit())
```

Output

```
True
```

---

# Check Letters and Numbers

```python
print("ABC123".isalnum())
```

Output

```
True
```

---

# Check Lowercase

```python
print("python".islower())
```

Output

```
True
```

---

# Check Uppercase

```python
print("PYTHON".isupper())
```

Output

```
True
```

---

# f-String Formatting

```python
name = "John"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

Output

```
My name is John.
I am 22 years old.
```

---

# format() Method

```python
name = "Alice"
age = 20

print("Name: {} Age: {}".format(name, age))
```

Output

```
Name: Alice Age: 20
```

---

# Loop Through a String

```python
word = "Python"

for letter in word:
    print(letter)
```

Output

```
P
y
t
h
o
n
```

---

# Reverse Using Loop

```python
word = "Python"

reverse = ""

for letter in word:
    reverse = letter + reverse

print(reverse)
```

Output

```
nohtyP
```

---

# Count Vowels

```python
text = "Programming"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)
```

Output

```
3
```

---

# Palindrome Example

```python
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

Output

```
Palindrome
```

---

# Remove All Spaces

```python
text = "Python Programming"

print(text.replace(" ", ""))
```

Output

```
PythonProgramming
```

---

# Common Mistakes

❌ Wrong

```python
age = 20

print("Age: " + age)
```

Error

```
TypeError
```

✅ Correct

```python
print("Age: " + str(age))
```

or

```python
print(f"Age: {age}")
```

---

# Quick Summary

| Function | Description |
|-----------|-------------|
| `len()` | Length of string |
| `upper()` | Uppercase |
| `lower()` | Lowercase |
| `capitalize()` | First letter uppercase |
| `title()` | Every word uppercase |
| `swapcase()` | Reverse case |
| `strip()` | Remove spaces |
| `replace()` | Replace text |
| `find()` | Find index |
| `count()` | Count occurrences |
| `split()` | Split into list |
| `join()` | Join list into string |
| `startswith()` | Starts with |
| `endswith()` | Ends with |
| `isalpha()` | Letters only |
| `isdigit()` | Numbers only |
| `isalnum()` | Letters and numbers |
| `islower()` | Check lowercase |
| `isupper()` | Check uppercase |

---

# Key Points

- A string is a sequence of characters.
- Strings are **immutable**, meaning they cannot be changed after creation.
- Use indexing to access characters.
- Use slicing to extract parts of a string.
- Use string methods to modify or check text.
- f-strings are the easiest way to format strings.
- Most string methods return a **new string** without changing the original.
# Variables in Python

## What is a Variable?

A variable is a named storage location used to hold data in memory. Variables allow a program to store, retrieve, and manipulate information during execution.

Example:                   

```python
name = "Tharuka"
age = 21
```

In this example:

* `name` stores a string value.
* `age` stores an integer value.

---

# Variable Naming Rules

## Valid Variable Names

```python
student_name = "John"
age = 20
total_marks = 450
_count = 5
```

### Rules

1. Variable names must start with:

   * A letter (A-Z, a-z)
   * An underscore (_)

2. Variable names cannot start with a number.

```python
2name = "John"   # Invalid
```

3. Variable names may contain:

   * Letters
   * Numbers
   * Underscores

```python
student1 = "John"
total_marks = 450
```

4. Variable names cannot contain spaces.

```python
student name = "John"  # Invalid
```

5. Variable names are case-sensitive.

```python
name = "John"
Name = "David"
```

These are treated as different variables.

---

# Reserved Keywords

Python keywords cannot be used as variable names.

Examples:

```python
class
if
else
for
while
return
import
def
```

Invalid:

```python
class = "Student"
```

---

# Variable Assignment

Assign a value using the assignment operator (=).

```python
name = "Tharuka"
age = 21
```

---

# Multiple Variable Assignment

```python
x, y, z = 10, 20, 30
```

---

# Assign Same Value to Multiple Variables

```python
a = b = c = 100
```

---

# Variable Types

## Integer (int)

Whole numbers.

```python
age = 21
count = 100
```

## Float (float)

Decimal numbers.

```python
price = 150.75
height = 5.8
```

## String (str)

Text data.

```python
name = "Tharuka"
```

## Boolean (bool)

True or False values.

```python
is_logged_in = True
is_admin = False
```

---

# Checking Variable Type

Use the `type()` function.

```python
age = 21
print(type(age))
```

Output:

```python
<class 'int'>
```

---

# Dynamic Typing

Python automatically determines the data type.

```python
value = 10
value = "Hello"
```

The variable can store different data types at different times.

---

# Constants

Python does not have true constants.

Use uppercase names to indicate values that should not change.

```python
PI = 3.14159
MAX_USERS = 100
```

---

# Naming Conventions

Use descriptive names.

Good:

```python
student_name = "John"
total_marks = 450
```

Bad:

```python
a = "John"
x = 450
```

---

# Best Practices

✅ Use meaningful names.

✅ Follow snake_case naming.

```python
student_name
total_marks
account_balance
```

✅ Keep variable names short but descriptive.

✅ Use constants for fixed values.

✅ Avoid single-letter variable names unless used in loops.

---

# Examples

```python
student_name = "Tharuka"
student_age = 21
course = "Python Programming"
is_active = True

print(student_name)
print(student_age)
print(course)
print(is_active)
```

Output:

```text
Tharuka
21
Python Programming
True
```

---

# Summary

Variables are used to store data in memory. Python variables are dynamically typed, easy to create, and follow specific naming rules. Using meaningful variable names and proper naming conventions improves code readability and maintainability.

"""
=========================================================
              PYTHON OPERATORS NOTES
=========================================================

What are Operators?
-------------------
Operators are special symbols or keywords used to perform
operations on variables and values.

Example:

a = 10
b = 5

result = a + b

Operators are divided into:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

=========================================================
"""


# =========================================================
# Example 1 - Arithmetic Operators
# =========================================================

# Arithmetic operators are used for calculations.

a = 10
b = 3

print("Example 1 - Arithmetic Operators")

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Modulus (remainder)
print("Modulus:", a % b)

# Floor Division
print("Floor Division:", a // b)

# Power
print("Power:", a ** b)


print("\n" + "=" * 50)



# =========================================================
# Example 2 - Assignment Operators
# =========================================================

# Assignment operators are used to assign values.

print("Example 2 - Assignment Operators")

x = 10

print("Original value:", x)


# x = x + 5
x += 5

print("After += 5:", x)


# x = x - 3
x -= 3

print("After -= 3:", x)


# x = x * 2
x *= 2

print("After *= 2:", x)


# x = x / 2
x /= 2

print("After /= 2:", x)



print("\n" + "=" * 50)



# =========================================================
# Example 3 - Multiple Assignment
# =========================================================

# Assign multiple values at once.

print("Example 3 - Multiple Assignment")

name, age, marks = "John", 22, 85

print(name)
print(age)
print(marks)



print("\n" + "=" * 50)



# =========================================================
# Example 4 - Comparison Operators
# =========================================================

# Comparison operators compare two values.
# Output is always True or False.

print("Example 4 - Comparison Operators")

a = 10
b = 5


print("Equal:", a == b)

print("Not Equal:", a != b)

print("Greater Than:", a > b)

print("Less Than:", a < b)

print("Greater or Equal:", a >= b)

print("Less or Equal:", a <= b)



print("\n" + "=" * 50)



# =========================================================
# Example 5 - Logical Operators
# =========================================================

# Logical operators combine conditions.

print("Example 5 - Logical Operators")


age = 20


# AND:
# Both conditions must be True

print(
    "AND:",
    age > 18 and age < 30
)



# OR:
# At least one condition must be True

print(
    "OR:",
    age < 18 or age > 60
)



# NOT:
# Reverse True to False

student = True

print(
    "NOT:",
    not student
)



print("\n" + "=" * 50)



# =========================================================
# Example 6 - Identity Operators
# =========================================================

# Identity operators check whether two variables
# refer to the same object in memory.

print("Example 6 - Identity Operators")


list1 = [1, 2, 3]

list2 = list1


print("list1 is list2:", list1 is list2)



list3 = [1, 2, 3]


print(
    "list1 is not list3:",
    list1 is not list3
)



print("\n" + "=" * 50)



# =========================================================
# Example 7 - Membership Operators
# =========================================================

# Membership operators check whether a value exists.

print("Example 7 - Membership Operators")


text = "Python Programming"


print(
    "Python in text:",
    "Python" in text
)


print(
    "Java in text:",
    "Java" in text
)


print(
    "Java not in text:",
    "Java" not in text
)



print("\n" + "=" * 50)



# =========================================================
# Example 8 - Bitwise Operators
# =========================================================

# Bitwise operators work with binary numbers.

print("Example 8 - Bitwise Operators")


a = 5
b = 3


# Binary:
#
# 5 = 101
# 3 = 011
#
# AND result:
# 001 = 1

print("AND (&):", a & b)


# OR:
# 111 = 7

print("OR (|):", a | b)


# XOR:
# 110 = 6

print("XOR (^):", a ^ b)


# NOT

print("NOT (~):", ~a)


# Left shift

print("Left Shift (<<):", a << 1)


# Right shift

print("Right Shift (>>):", a >> 1)



print("\n" + "=" * 50)



# =========================================================
# Example 9 - Operator Precedence
# =========================================================

# Python follows priority rules.
# Multiplication happens before addition.

print("Example 9 - Operator Precedence")


result = 10 + 5 * 2


print(result)


# Calculation:
#
# 5 * 2 = 10
# 10 + 10 = 20



print("\n" + "=" * 50)



# =========================================================
# Example 10 - Real Example (Student Grade Checker)
# =========================================================

print("Example 10 - Student Grade Checker")


marks = 75


if marks >= 50 and marks <= 100:

    print("Student Passed")


else:

    print("Student Failed")



print("\n" + "=" * 50)



# =========================================================
# Example 11 - Simple Calculator Using Operators
# =========================================================

print("Example 11 - Calculator")


num1 = 20
num2 = 5


print("Addition:", num1 + num2)

print("Subtraction:", num1 - num2)

print("Multiplication:", num1 * num2)

print("Division:", num1 / num2)



print("\n" + "=" * 50)



"""
=========================================================
                  QUICK SUMMARY
=========================================================


Arithmetic Operators:
    +   Addition
    -   Subtraction
    *   Multiplication
    /   Division
    %   Remainder
    //  Floor Division
    **  Power


Assignment Operators:
    =
    +=
    -=
    *=
    /=


Comparison Operators:
    ==
    !=
    >
    <
    >=
    <=


Logical Operators:
    and
    or
    not


Identity Operators:
    is
    is not


Membership Operators:
    in
    not in


Bitwise Operators:
    &
    |
    ^
    ~
    <<
    >>


=========================================================

Operators are used in almost every Python program.

=========================================================
"""


print("End of Python Operators Notes.")
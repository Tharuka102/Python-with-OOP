"""
=========================================================
        PYTHON USER INPUT NOTES (input() Function)
=========================================================

This file explains how to use the input() function in Python.

What is input()?
----------------
- input() pauses the program and waits for the user to type something.
- After the user presses Enter, the value is returned to the program.
- The returned value is ALWAYS a STRING (str).

Syntax:
    variable = input("Enter something: ")

Example:
    name = input("Enter your name: ")
    print("Hello,", name)

=========================================================
"""

# =========================================================
# Example 1 - Basic Input and Output
# =========================================================

# input() asks the user to enter their name.
# Whatever the user types is stored as a string.

name = input("Example 1 - Enter your name: ")
print("Hello,", name)

print("\n" + "=" * 50)


# =========================================================
# Example 2 - input() Always Returns a String
# =========================================================

# Even if the user types a number,
# Python stores it as a string.

age = input("Example 2 - Enter your age: ")

print("Value entered:", age)
print("Data type:", type(age))     # Output: <class 'str'>

print("\n" + "=" * 50)


# =========================================================
# Example 3 - Convert String to Integer (Type Casting)
# =========================================================

# To perform mathematical operations,
# convert the string into an integer.

age = input("Example 3 - Enter your age again: ")

age = int(age)     # Convert string -> integer

print("Next year you will be", age + 1)

print("\n" + "=" * 50)


# =========================================================
# Example 4 - Adding Two Numbers
# =========================================================

# Without int(), Python joins strings instead of adding numbers.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = int(num1) + int(num2)

print("Sum =", result)

print("\n" + "=" * 50)


# =========================================================
# Example 5 - Common Mistake (String Concatenation)
# =========================================================

# Here we DO NOT convert to int().
# If the user enters:
# 5
# 3
#
# Output will be:
# 53
#
# because Python joins two strings.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Without int():", num1 + num2)

print("\n" + "=" * 50)


# =========================================================
# Example 6 - Float Input
# =========================================================

# Use float() when decimal values are needed.

height = input("Enter your height in meters: ")

height = float(height)

print("Your height is", height, "meters")

print("\n" + "=" * 50)


# =========================================================
# Example 7 - Multiple Inputs in One Line
# =========================================================

# split() separates values using spaces.

data = input("Enter your name and age (Example: John 22): ")

name, age = data.split()

age = int(age)

print(f"{name} is {age} years old.")

print("\n" + "=" * 50)


# =========================================================
# Example 8 - Input a List of Numbers
# =========================================================

# User enters numbers separated by spaces.
# split() creates a list of strings.
# List comprehension converts every item into an integer.

numbers = input("Enter numbers separated by spaces: ")

numbers_list = numbers.split()

numbers_list = [int(n) for n in numbers_list]

print("Numbers:", numbers_list)
print("Sum =", sum(numbers_list))

print("\n" + "=" * 50)


# =========================================================
# Example 9 - Handling Invalid Input (try-except)
# =========================================================

# If the user enters letters instead of numbers,
# int() causes a ValueError.
#
# try-except prevents the program from crashing.

try:
    age = int(input("Enter your age: "))
    print("Your age is", age)

except ValueError:
    print("Error: Please enter a valid number.")

print("\n" + "=" * 50)


# =========================================================
# Example 10 - Simple Calculator
# =========================================================

# This program takes two numbers and an operator
# then performs the selected calculation.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero.")

else:
    print("Invalid operator.")

print("\n" + "=" * 50)


# =========================================================
# QUICK SUMMARY
# =========================================================

"""
1. input() waits for user input.

2. input() ALWAYS returns a string (str).

3. Use int() to convert whole numbers.
      age = int(input("Enter age: "))

4. Use float() for decimal numbers.
      price = float(input("Enter price: "))

5. Use split() to read multiple values.
      name, age = input().split()

6. Use try-except to handle invalid input safely.

7. Without int() or float():
      "5" + "3" = "53"

   With int():
      5 + 3 = 8
"""

print("End of Python User Input Notes.")
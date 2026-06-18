# Python User Input Notes

## What is `input()`?

The `input()` function lets a Python program pause and wait for the user to type something on the keyboard. 
Whatever the user types is sent back to the program as **text** (a string), even if the user types numbers.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Output:**
```
Enter your name: John
Hello, John
```

---

## Key Rule: `input()` Always Returns a String

No matter what the user types — a number, a word, anything — Python stores it as type `str`.

```python
age = input("Enter your age: ")
print(type(age))   # <class 'str'>  -- even if the user typed "25"
```

This means if you want to do math with the input, you must convert it first using `int()` or `float()`. 
(See the Type Casting notes for more on this.)

```python
age = input("Enter your age: ")
age = int(age)              # convert string to integer

print("Next year you'll be:", age + 1)
```

---

## Example 1: Basic Input and Output

```python
city = input("Which city do you live in? ")
print("You live in", city)
```

---

## Example 2: Input with Numbers (Casting Required)

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Without casting, this would join the strings together (e.g. "5" + "3" = "53")
result = int(num1) + int(num2)

print("Sum:", result)
```

**Without casting (common mistake):**
```python
num1 = input("Enter first number: ")  # "5"
num2 = input("Enter second number: ")  # "3"

print(num1 + num2)   # "53"  -- string concatenation, NOT addition!
```

---

## Example 3: Input with Float Numbers

```python
height = input("Enter your height in meters: ")
height = float(height)

print("Your height is", height, "meters")
```

---

## Example 4: Multiple Inputs in One Line

You can use `split()` to take multiple values from a single line of input.

```python
data = input("Enter your name and age separated by a space: ")
name, age = data.split()

age = int(age)
print(f"{name} is {age} years old.")
```

**Example run:**
```
Enter your name and age separated by a space: Kavindu 22
Kavindu is 22 years old.
```

---

## Example 5: Taking a List of Numbers from One Line

```python
numbers = input("Enter numbers separated by spaces: ")
numbers_list = numbers.split()              # splits into a list of strings
numbers_list = [int(n) for n in numbers_list]  # convert each to int

print("Sum:", sum(numbers_list))
```

**Example run:**
```
Enter numbers separated by spaces: 1 2 3 4 5
Sum: 15
```

---

## Example 6: Handling Invalid Input Safely

If the user types something that can't be converted (e.g., letters instead of numbers), `int()` will raise a `ValueError`. Use `try-except` to handle this.

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("That's not a valid number!")
```

---

## Example 7: Simple Input-Based Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
```

---

## Quick Summary

- `input("message")` shows a prompt and waits for the user to type something, then press Enter.
- The value returned by `input()` is **always a string**, even if it looks like a number.
- To do math, convert the input using `int()` or `float()`.
- Use `.split()` to break one line of input into multiple values.
- Use `try-except` around `int()`/`float()` conversions to avoid crashes from invalid input.
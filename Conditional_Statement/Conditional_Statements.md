# Python Conditional Statements

Conditional statements are used in Python to make decisions based on certain conditions.

They allow a program to execute different blocks of code depending on whether a condition is **True** or **False**.

Python uses comparison operators and logical operators to create conditions.

---

# 1. What is a Condition?

A condition is an expression that gives one of two results:

- `True` → Condition is satisfied
- `False` → Condition is not satisfied

Example:

```python
age = 18

print(age >= 18)
```

Output:

```
True
```

Because 18 is greater than or equal to 18.

---

# 2. Comparison Operators

Comparison operators are used to compare values.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | x == 10 |
| `!=` | Not equal to | x != 10 |
| `>` | Greater than | x > 10 |
| `<` | Less than | x < 10 |
| `>=` | Greater than or equal | x >= 10 |
| `<=` | Less than or equal | x <= 10 |

Example:

```python
x = 20

if x > 10:
    print("x is greater than 10")
```

Output:

```
x is greater than 10
```

---

# 3. Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both conditions must be True | x > 5 and x < 20 |
| `or` | At least one condition True | x > 5 or x < 2 |
| `not` | Reverse the condition | not(x > 5) |

Example:

```python
age = 20

if age >= 18 and age <= 60:
    print("Adult")
```

Output:

```
Adult
```

---

# 4. if Statement

## Theory

The `if` statement is used when we want to execute a block of code only when a condition is True.

If the condition is False, the code block will be skipped.

## Syntax

```python
if condition:
    statement
```

**Important:**
- Python uses indentation to define code blocks.
- The colon `:` is required after the condition.

---

## Example

```python
temperature = 35

if temperature > 30:
    print("Weather is hot")
```

Output:

```
Weather is hot
```

---

## Example 2

```python
marks = 75

if marks >= 50:
    print("Pass")
```

Output:

```
Pass
```

---

# 5. if-else Statement

## Theory

The `if-else` statement is used when there are two possible outcomes.

- If condition is True → Execute if block
- If condition is False → Execute else block

## Syntax

```python
if condition:
    statement 1
else:
    statement 2
```

---

## Example

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

Output:

```
You cannot vote
```

---

## Example 2: Check Even or Odd Number

```python
number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

Output:

```
Even Number
```

---

# 6. if-elif-else Statement

## Theory

The `if-elif-else` statement is used when we have multiple conditions.

- `if` checks the first condition
- `elif` checks another condition if the previous condition is False
- `else` runs when all conditions are False

## Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

---

## Example: Student Grade System

```python
marks = 85

if marks >= 75:
    print("Grade A")

elif marks >= 65:
    print("Grade B")

elif marks >= 55:
    print("Grade C")

else:
    print("Fail")
```

Output:

```
Grade A
```

---

# 7. Multiple elif Conditions

Example:

```python
number = 0

if number > 0:
    print("Positive Number")

elif number < 0:
    print("Negative Number")

else:
    print("Zero")
```

Output:

```
Zero
```

---

# 8. Nested Conditions

## Theory

A nested condition means placing one conditional statement inside another conditional statement.

It is useful when we need to check multiple levels of decisions.

## Syntax

```python
if condition1:

    if condition2:
        statement

    else:
        statement

else:
    statement
```

---

## Example

```python
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed")

    else:
        print("ID required")

else:
    print("Under age")
```

Output:

```
Entry allowed
```

---

# 9. Conditional Statements with User Input

Example:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")

else:
    print("Child")
```

Example Output:

```
Enter your age: 22
Adult
```

---

# 10. Short Hand if Statement

Python allows writing simple if statements in one line.

Example:

```python
x = 10

if x > 5:
    print("Greater")
```

Short version:

```python
x = 10

print("Greater") if x > 5 else print("Smaller")
```

---

# 11. Membership Conditions

Python can check whether a value exists in a collection.

Operators:

- `in`
- `not in`

Example:

```python
fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("Apple is available")
```

Output:

```
Apple is available
```

---

# 12. Identity Conditions

Identity operators:

- `is`
- `is not`

They check whether two objects are the same object.

Example:

```python
x = None

if x is None:
    print("No value")
```

Output:

```
No value
```

---

# 13. Difference Between if, if-else and if-elif-else

| Statement | Usage |
|-----------|-------|
| if | Used for one condition |
| if-else | Used for two choices |
| if-elif-else | Used for multiple choices |
| Nested if | Used for conditions inside conditions |

---

# 14. Real World Example

## Login System

```python
username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("User Not Found")
```

Output:

```
Login Successful
```

---

# 15. Common Mistakes

## 1. Forgetting colon (:)

Wrong:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## 2. Wrong indentation

Wrong:

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

---

## 3. Using = instead of ==

Wrong:

```python
if x = 10:
```

Correct:

```python
if x == 10:
```

`=` → Assignment  
`==` → Comparison

---

# 16. Practice Questions

### Question 1

Write a program to check whether a person can vote.

Requirements:

- Input age
- If age >= 18 print "Eligible"
- Otherwise print "Not Eligible"

---

### Question 2

Create a grade calculator.

Conditions:

```
75 - 100 : A
65 - 74  : B
55 - 64  : C
Below 55 : Fail
```

---

### Question 3

Create a login system using nested if.

Username:

```
admin
```

Password:

```
12345
```

---

# Summary

Python Conditional Statements:

1. **if**
   - Executes code when condition is True.

2. **if-else**
   - Selects between two choices.

3. **if-elif-else**
   - Handles multiple conditions.

4. **Nested Conditions**
   - Conditional statements inside another condition.

Conditional statements help programs make decisions and control program flow.
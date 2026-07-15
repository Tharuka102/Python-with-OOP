# Python Loops

Loops are used in Python to execute a block of code repeatedly until a specific condition is satisfied.

Instead of writing the same code multiple times, loops help us reduce code repetition and make programs more efficient.

Python mainly has two types of loops:

1. **for loop**
2. **while loop**

Python also provides loop control statements:

- `break`
- `continue`
- `pass`

---

# 1. What is a Loop?

A loop is a programming structure that repeats a set of instructions multiple times.

### Example Without Loop:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

This creates code repetition.

Using a loop:

```python
for i in range(5):
    print("Hello")
```

Output:

```
Hello
Hello
Hello
Hello
Hello
```

---

# 2. for Loop

## Theory

A `for` loop is used to iterate over a sequence.

A sequence can be:

- List
- Tuple
- String
- Range
- Dictionary
- Set

The `for` loop runs once for each item in the sequence.

---

## Syntax

```python
for variable in sequence:
    statement
```

---

# Example 1: Loop Through a List

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```
Apple
Banana
Orange
```

---

# Example 2: Using range()

The `range()` function generates a sequence of numbers.

Syntax:

```python
range(start, stop, step)
```

- start → Starting value
- stop → Ending value (not included)
- step → Increment value

---

Example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```
1
2
3
4
5
```

---

# Example 3: Using Step Value

```python
for number in range(0, 10, 2):
    print(number)
```

Output:

```
0
2
4
6
8
```

---

# Example 4: Loop Through String

```python
name = "Python"

for letter in name:
    print(letter)
```

Output:

```
P
y
t
h
o
n
```

---

# 3. while Loop

## Theory

A `while` loop executes a block of code as long as the condition is True.

The loop stops when the condition becomes False.

---

## Syntax

```python
while condition:
    statement
```

---

# Example 1

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# Example 2: User Input with while Loop

```python
number = 1

while number != 0:

    number = int(input("Enter number (0 to stop): "))

    print("You entered:", number)
```

Output:

```
Enter number (0 to stop): 5
You entered: 5

Enter number (0 to stop): 0
You entered: 0
```

---

# Difference Between for Loop and while Loop

| for loop | while loop |
|----------|------------|
| Used when number of iterations is known | Used when number of iterations is unknown |
| Works with sequences | Works with conditions |
| Automatically updates iteration | Programmer must update condition |
| Example: range() | Example: user input loop |

---

# 4. break Statement

## Theory

The `break` statement is used to immediately stop a loop.

When Python finds `break`, it exits the loop completely.

---

## Example

```python
for number in range(1, 10):

    if number == 5:
        break

    print(number)
```

Output:

```
1
2
3
4
```

Explanation:

When number becomes 5, the loop stops.

---

# Example: while loop with break

```python
while True:

    user_input = input("Enter 'exit' to stop: ")

    if user_input == "exit":
        break

    print(user_input)
```

---

# 5. continue Statement

## Theory

The `continue` statement skips the current iteration and moves to the next iteration.

The loop does not stop.

---

## Example

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

Output:

```
1
2
4
5
```

Explanation:

When number is 3, Python skips printing and continues.

---

# Example: Print Only Even Numbers

```python
for number in range(1, 10):

    if number % 2 != 0:
        continue

    print(number)
```

Output:

```
2
4
6
8
```

---

# 6. pass Statement

## Theory

The `pass` statement is a null statement.

It does nothing when executed.

It is used as a placeholder when we need an empty block of code.

---

## Example

```python
for number in range(5):

    if number == 3:
        pass

    print(number)
```

Output:

```
0
1
2
3
4
```

---

# Example: Empty Function

```python
def future_function():
    pass
```

The function does nothing but does not create an error.

---

# 7. Nested Loops

## Theory

A loop inside another loop is called a nested loop.

The inner loop runs completely for each iteration of the outer loop.

---

## Example

```python
for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)
```

Output:

```
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

# 8. Loop with else

Python allows using `else` with loops.

The else block executes when the loop finishes normally.

---

## Example

```python
for number in range(5):

    print(number)

else:

    print("Loop Finished")
```

Output:

```
0
1
2
3
4
Loop Finished
```

---

# 9. Common Loop Mistakes

## 1. Infinite while Loop

Wrong:

```python
count = 1

while count <= 5:
    print(count)
```

Problem:

The value of `count` never changes.

Correct:

```python
count = 1

while count <= 5:

    print(count)

    count += 1
```

---

## 2. Wrong Indentation

Wrong:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

# 10. Practice Questions

## Question 1

Print numbers from 1 to 10 using a for loop.

---

## Question 2

Create a program to find the sum of numbers from 1 to 100 using a while loop.

---

## Question 3

Print numbers from 1 to 10 but skip number 5 using continue.

---

## Question 4

Create a program that stops when the user enters 0 using break.

---

# Summary

## for Loop

- Used for iterating through sequences.
- Best when the number of iterations is known.

## while Loop

- Runs while a condition is True.
- Best when the number of iterations is unknown.

## break

- Stops the loop completely.

## continue

- Skips the current iteration.

## pass

- Does nothing.
- Used as a placeholder.

Loops are important because they help automate repeated tasks and make programs shorter and more efficient.
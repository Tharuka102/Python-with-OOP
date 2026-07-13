# Python Operators Notes

## What are Operators?

Operators are special symbols or keywords used to perform operations on values and variables.

Example:

```python
a = 10
b = 5

result = a + b

print(result)
```

Output:

```
15
```

Python has different types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Modulus (remainder) | `10 % 3` |
| `//` | Floor Division | `10 // 3` |
| `**` | Power | `2 ** 3` |

---

## Addition (+)

```python
a = 10
b = 5

result = a + b

print(result)
```

Output:

```
15
```

---

## Subtraction (-)

```python
a = 10
b = 5

print(a - b)
```

Output:

```
5
```

---

## Multiplication (*)

```python
a = 10
b = 5

print(a * b)
```

Output:

```
50
```

---

## Division (/)

```python
a = 10
b = 2

print(a / b)
```

Output:

```
5.0
```

Note:

`/` always returns a float.

---

## Modulus (%)

Returns the remainder after division.

```python
number = 10

print(number % 3)
```

Output:

```
1
```

Explanation:

```
10 ÷ 3 = 3 remainder 1
```

---

## Floor Division (//)

Removes the decimal part.

```python
result = 10 // 3

print(result)
```

Output:

```
3
```

---

## Power (**)

Used to calculate exponent.

```python
result = 2 ** 3

print(result)
```

Output:

```
8
```

Explanation:

```
2 × 2 × 2 = 8
```

---

# 2. Assignment Operators

Assignment operators assign values to variables.

| Operator | Example | Same As |
|----------|---------|---------|
| `=` | x = 5 | Assign value |
| `+=` | x += 5 | x = x + 5 |
| `-=` | x -= 5 | x = x - 5 |
| `*=` | x *= 5 | x = x * 5 |
| `/=` | x /= 5 | x = x / 5 |
| `%=` | x %= 5 | x = x % 5 |
| `//=` | x //= 5 | x = x // 5 |
| `**=` | x **= 5 | x = x ** 5 |

---

## Assignment Example

```python
x = 10

x += 5

print(x)
```

Output:

```
15
```

Explanation:

```
x = x + 5
x = 10 + 5
```

---

## Multiple Assignment

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

Output:

```
10
20
30
```

---

# 3. Comparison Operators

Comparison operators compare two values.

The output is always:

```
True
or
False
```

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater or equal |
| `<=` | Less or equal |

---

## Equal (==)

```python
a = 10
b = 10

print(a == b)
```

Output:

```
True
```

---

## Not Equal (!=)

```python
a = 10
b = 5

print(a != b)
```

Output:

```
True
```

---

## Greater Than (>)

```python
print(10 > 5)
```

Output:

```
True
```

---

## Less Than (<)

```python
print(5 < 10)
```

Output:

```
True
```

---

## Greater or Equal (>=)

```python
age = 18

print(age >= 18)
```

Output:

```
True
```

---

## Less or Equal (<=)

```python
marks = 50

print(marks <= 100)
```

Output:

```
True
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| `and` | Both conditions must be True |
| `or` | At least one condition True |
| `not` | Reverse the result |

---

# AND Operator

Both conditions must be true.

```python
age = 20

print(age > 18 and age < 30)
```

Output:

```
True
```

---

# OR Operator

Only one condition needs to be true.

```python
age = 15

print(age < 18 or age > 60)
```

Output:

```
True
```

---

# NOT Operator

Reverses the result.

```python
is_student = True

print(not is_student)
```

Output:

```
False
```

---

# 5. Identity Operators

Identity operators compare whether two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| `is` | Same object |
| `is not` | Different object |

---

## is Operator

```python
a = [1,2,3]
b = a

print(a is b)
```

Output:

```
True
```

---

## is not Operator

```python
a = [1,2,3]
b = [1,2,3]

print(a is not b)
```

Output:

```
True
```

Note:

Two lists can have the same values but different memory locations.

---

# 6. Membership Operators

Used to check whether a value exists inside a collection.

| Operator | Description |
|----------|-------------|
| `in` | Exists |
| `not in` | Does not exist |

---

## in Operator

```python
text = "Python"

print("P" in text)
```

Output:

```
True
```

---

## not in Operator

```python
text = "Python"

print("Java" not in text)
```

Output:

```
True
```

---

# 7. Bitwise Operators

Bitwise operators work with binary numbers.

| Operator | Name |
|----------|------|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

---

# Bitwise AND (&)

```python
a = 5
b = 3

print(a & b)
```

Binary:

```
5 = 101
3 = 011

AND = 001
```

Output:

```
1
```

---

# Bitwise OR (|)

```python
print(5 | 3)
```

Output:

```
7
```

---

# Bitwise XOR (^)

```python
print(5 ^ 3)
```

Output:

```
6
```

---

# Bitwise NOT (~)

```python
print(~5)
```

Output:

```
-6
```

---

# Left Shift (<<)

Moves bits left.

```python
print(5 << 1)
```

Output:

```
10
```

---

# Right Shift (>>)

Moves bits right.

```python
print(10 >> 1)
```

Output:

```
5
```

---

# Operator Precedence

Python follows an order when multiple operators are used.

Order:

```
()
**
+x  -x
* / // %
+ -
<< >>
&
^
|
==
!=
>
<
>=
<=
not
and
or
```

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```
20
```

Explanation:

Multiplication happens first:

```
5 * 2 = 10

10 + 10 = 20
```

---

# Real Example - Student Grade Checker

```python
marks = 75

if marks >= 50 and marks <= 100:
    print("Pass")

else:
    print("Fail")
```

Output:

```
Pass
```

---

# Quick Summary

| Type | Operators |
|-|-|
| Arithmetic | `+ - * / % // **` |
| Assignment | `= += -= *= /=` |
| Comparison | `== != > < >= <=` |
| Logical | `and or not` |
| Identity | `is is not` |
| Membership | `in not in` |
| Bitwise | `& | ^ ~ << >>` |

---

# Key Points

- Operators perform operations on values.
- Arithmetic operators perform calculations.
- Comparison operators return True or False.
- Logical operators combine conditions.
- Identity operators compare objects.
- Membership operators check values inside collections.
- Bitwise operators work with binary numbers.
- Operator precedence decides the order of calculations.
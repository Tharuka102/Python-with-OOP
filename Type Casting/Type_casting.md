# Python Type Casting Notes

## What is Type Casting?

Type casting (type conversion) means converting one data type into another data type. 
For example, converting a `string` into an `int`, or an `int` into a `float`.

In Python, type casting happens in two ways:

1. **Implicit Type Casting** – Python automatically converts one type to another (no action needed from the programmer).
2. **Explicit Type Casting** – The programmer manually converts a type using built-in functions like `int()`, `float()`, `str()`.

---

## 1. Implicit Type Casting

Python automatically converts data types when it's safe to do so (e.g., `int` -> `float`), without losing any data.

```python
num_int = 10
num_float = 2.5

# Python automatically converts int to float before adding
result = num_int + num_float

print(result)        # 12.5
print(type(result))  # <class 'float'>
```

**Note:** Implicit casting only happens for "safe" conversions (like `int` -> `float`). 
Python will NOT implicitly convert `str` -> `int` — that raises an error.

```python
num = 5
text = "10"

result = num + text   # ❌ TypeError: unsupported operand type(s)
```

---

## 2. Explicit Type Casting

Here, the programmer manually converts a type using built-in functions.

### Commonly Used Functions

| Function | Use |
|---|---|
| `int()` | Converts another type into an integer |
| `float()` | Converts another type into a float |
| `str()` | Converts another type into a string |
| `bool()` | Converts another type into a boolean |
| `list()` | Converts another type into a list |
| `tuple()` | Converts another type into a tuple |

### Example 1: String to Integer

```python
age_str = "25"
age_int = int(age_str)

print(age_int)        # 25
print(type(age_int))  # <class 'int'>
```

### Example 2: Integer to Float

```python
num = 7
num_float = float(num)

print(num_float)        # 7.0
print(type(num_float))  # <class 'float'>
```

### Example 3: Float to Integer (Decimal Part Lost)

```python
price = 99.99
price_int = int(price)

print(price_int)  # 99   (the decimal part is truncated, not rounded)
```

### Example 4: Integer/Float to String

```python
score = 95
score_str = str(score)

print(score_str)        # "95"
print(type(score_str))  # <class 'str'>

# This is needed for string concatenation
print("Your score is: " + score_str)
```

### Example 5: String to Float

```python
height_str = "5.9"
height_float = float(height_str)

print(height_float)  # 5.9
```

### Example 6: Boolean Casting

```python
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False (empty string)
print(bool("Hi"))   # True  (non-empty string)
print(bool([]))     # False (empty list)
print(bool([1,2]))  # True  (non-empty list)
```

### Example 7: List, Tuple, Set Conversions

```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)        # [1, 2, 3]
print(type(my_list))  # <class 'list'>

my_set = set(my_list)
print(my_set)          # {1, 2, 3}
print(type(my_set))    # <class 'set'>
```

---

## Common Error: Invalid Casting

If a string doesn't actually contain a valid number, using `int()` or `float()` on it raises an error.

```python
value = "hello"
num = int(value)   # ❌ ValueError: invalid literal for int() with base 10: 'hello'
```

**Fix:** Use try-except to handle this safely.

```python
value = "hello"

try:
    num = int(value)
except ValueError:
    print("Conversion failed — this is not a valid number")
```

---

## Real Example: Taking User Input and Casting

The `input()` function always returns a **string**. That's why you need to cast it with `int()` or `float()` before doing calculations.

```python
# get the user's age
age = input("Enter your age: ")   # type: str

age = int(age)                    # explicit cast to int

next_year_age = age + 1
print("Next year you will be:", next_year_age)
```

---

## Quick Summary

- **Implicit casting** → Python does this automatically, only for safe conversions.
- **Explicit casting** → The programmer does this manually using functions like `int()`, `float()`, `str()`, `bool()`, `list()`.
- Converting `float` -> `int` **truncates** the decimal part (it does not round).
- Casting an invalid string (e.g. `"hello"`) to a number raises a **ValueError**.
- Data from `input()` is always type `str` — cast it before using it in calculations.
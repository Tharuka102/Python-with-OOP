"""
=========================================================
           PYTHON TYPE CASTING NOTES
=========================================================

What is Type Casting?
---------------------
Type casting (type conversion) means converting one data type
into another data type.

Examples:
    String  -> Integer
    Integer -> Float
    Float   -> Integer
    Integer -> String

Python supports two types of casting:

1. Implicit Type Casting
   - Python automatically converts data types.

2. Explicit Type Casting
   - The programmer manually converts data types using
     functions like:
        int()
        float()
        str()
        bool()
        list()
        tuple()
        set()

=========================================================
"""

# =========================================================
# Example 1 - Implicit Type Casting
# =========================================================

# Python automatically converts an integer into a float
# before performing the addition.

num_int = 10
num_float = 2.5

result = num_int + num_float

print("Example 1")
print("Result:", result)
print("Type:", type(result))

print("\n" + "=" * 50)


# =========================================================
# Example 2 - Implicit Casting Does NOT Work with Strings
# =========================================================

# Python cannot automatically convert a string into a number.

num = 5
text = "10"

# Uncomment the line below to see the error.

# result = num + text
# TypeError:
# unsupported operand type(s) for +: 'int' and 'str'

print("Example 2")
print("Python cannot automatically convert")
print("String -> Integer")

print("\n" + "=" * 50)


# =========================================================
# Example 3 - String to Integer
# =========================================================

# int() converts a string into an integer.

age_str = "25"

age_int = int(age_str)

print("Example 3")
print(age_int)
print(type(age_int))

print("\n" + "=" * 50)


# =========================================================
# Example 4 - Integer to Float
# =========================================================

# float() converts an integer into a decimal number.

num = 7

num_float = float(num)

print("Example 4")
print(num_float)
print(type(num_float))

print("\n" + "=" * 50)


# =========================================================
# Example 5 - Float to Integer
# =========================================================

# int() removes the decimal part.
# It DOES NOT round the number.

price = 99.99

price_int = int(price)

print("Example 5")
print("Original:", price)
print("After int():", price_int)

print("\n" + "=" * 50)


# =========================================================
# Example 6 - Integer to String
# =========================================================

# str() converts numbers into text.

score = 95

score_str = str(score)

print("Example 6")
print(score_str)
print(type(score_str))

# Now string concatenation works.
print("Your score is: " + score_str)

print("\n" + "=" * 50)


# =========================================================
# Example 7 - String to Float
# =========================================================

height_str = "5.9"

height_float = float(height_str)

print("Example 7")
print(height_float)
print(type(height_float))

print("\n" + "=" * 50)


# =========================================================
# Example 8 - Boolean Casting
# =========================================================

# bool() converts values into True or False.

print("Example 8")

print("bool(0) =", bool(0))
print("bool(1) =", bool(1))

print("bool('') =", bool(""))
print("bool('Hello') =", bool("Hello"))

print("bool([]) =", bool([]))
print("bool([1,2]) =", bool([1,2]))

print("\n" + "=" * 50)


# =========================================================
# Example 9 - List, Tuple and Set Conversion
# =========================================================

# Convert tuple -> list

my_tuple = (1, 2, 3)

my_list = list(my_tuple)

print("Example 9")
print(my_list)
print(type(my_list))

# Convert list -> set

my_set = set(my_list)

print(my_set)
print(type(my_set))

print("\n" + "=" * 50)


# =========================================================
# Example 10 - Invalid Type Casting
# =========================================================

# "hello" cannot be converted into an integer.

value = "hello"

try:
    number = int(value)

except ValueError:
    print("Example 10")
    print("Conversion failed.")
    print("This is not a valid number.")

print("\n" + "=" * 50)


# =========================================================
# Example 11 - Real Example Using input()
# =========================================================

# input() always returns a string.
# We convert it into an integer before doing math.

age = input("Enter your age: ")

age = int(age)

next_year = age + 1

print("Next year you will be", next_year)

print("\n" + "=" * 50)


# =========================================================
# Example 12 - Multiple Type Castings
# =========================================================

number = 10

print("Example 12")

print("Original value:", number)
print("Original type:", type(number))

# Integer -> Float
number_float = float(number)

print(number_float)
print(type(number_float))

# Float -> String
number_string = str(number_float)

print(number_string)
print(type(number_string))

print("\n" + "=" * 50)


# =========================================================
# QUICK REFERENCE TABLE
# =========================================================

print("""
Common Type Casting Functions

int(value)      -> Convert to Integer
float(value)    -> Convert to Float
str(value)      -> Convert to String
bool(value)     -> Convert to Boolean
list(value)     -> Convert to List
tuple(value)    -> Convert to Tuple
set(value)      -> Convert to Set
""")

print("=" * 50)


# =========================================================
# QUICK SUMMARY
# =========================================================

"""
1. Type casting means converting one data type into another.

2. Python supports:
      • Implicit Casting
      • Explicit Casting

3. Implicit casting happens automatically.
      Example:
          int -> float

4. Explicit casting is done manually.
      int()
      float()
      str()
      bool()
      list()
      tuple()
      set()

5. float -> int removes the decimal part.
      99.99 -> 99

6. Invalid conversions raise ValueError.

7. input() always returns a string.

8. Convert user input before calculations.
      age = int(input("Enter age: "))

"""

print("End of Python Type Casting Notes.")
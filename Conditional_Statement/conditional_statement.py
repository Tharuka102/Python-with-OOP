# ==========================================
# Python Conditional Statements
# Topics:
# 1. if Statement
# 2. if-else Statement
# 3. if-elif-else Statement
# 4. Nested Conditions
# ==========================================


# ------------------------------------------
# 1. if Statement
# ------------------------------------------
# Theory:
# The if statement is used to execute a block
# of code only when the condition is True.
#
# Syntax:
# if condition:
#       statement


age = 20

# Check whether age is greater than or equal to 18
if age >= 18:
    print("You are eligible to vote")


# Output:
# You are eligible to vote



# ------------------------------------------
# 2. if-else Statement
# ------------------------------------------
# Theory:
# if-else is used when there are two possible
# outcomes.
#
# If the condition is True:
#     if block executes
#
# If the condition is False:
#     else block executes


marks = 40

# Check whether student passed or failed
if marks >= 50:
    print("Student Passed")

else:
    print("Student Failed")


# Output:
# Student Failed



# ------------------------------------------
# 3. if-elif-else Statement
# ------------------------------------------
# Theory:
# if-elif-else is used when we have multiple
# conditions.
#
# Python checks conditions from top to bottom.
# The first True condition will execute.


student_marks = 85


# Grade calculation
if student_marks >= 75:
    print("Grade A")

elif student_marks >= 65:
    print("Grade B")

elif student_marks >= 55:
    print("Grade C")

else:
    print("Fail")


# Output:
# Grade A



# ------------------------------------------
# 4. Nested Conditions
# ------------------------------------------
# Theory:
# Nested conditions mean placing one condition
# inside another condition.
#
# It is useful when a second decision depends
# on the first decision.


user_age = 22
has_ticket = True


# First check age
if user_age >= 18:

    # Second condition inside first condition
    if has_ticket:
        print("You can enter the event")

    else:
        print("Ticket required")

else:
    print("You are under age")


# Output:
# You can enter the event



# ------------------------------------------
# 5. Conditional Statement with User Input
# ------------------------------------------
# input() gets data from the user.
# int() converts string input into integer.


number = int(input("Enter a number: "))


# Check whether number is positive or negative

if number > 0:
    print("Positive Number")

elif number < 0:
    print("Negative Number")

else:
    print("Zero")


# ------------------------------------------
# 6. Even or Odd Number Checking
# ------------------------------------------
# Modulus operator (%) gives the remainder.
#
# If remainder is 0, number is even.


num = int(input("Enter a number to check even or odd: "))


if num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")



# ------------------------------------------
# 7. Logical Operators with Conditions
# ------------------------------------------
# and  -> Both conditions must be True
# or   -> At least one condition must be True
# not  -> Reverse the condition


temperature = 30


if temperature >= 20 and temperature <= 35:
    print("Normal Temperature")

else:
    print("Extreme Temperature")



# ------------------------------------------
# 8. Membership Condition
# ------------------------------------------
# "in" checks whether a value exists
# inside a collection.


fruits = ["apple", "banana", "orange"]


if "apple" in fruits:
    print("Apple is available")



# ------------------------------------------
# 9. Login System Example
# ------------------------------------------
# Using nested if conditions
# to check username and password.


username = "admin"
password = "12345"


if username == "admin":

    # Check password after username validation
    if password == "12345":
        print("Login Successful")

    else:
        print("Incorrect Password")

else:
    print("User Not Found")



# ------------------------------------------
# 10. Short Hand Conditional Statement
# ------------------------------------------
# Used for simple one-line decisions.


value = 10


print("Value is greater than 5") if value > 5 else print("Value is smaller")



# ==========================================
# End of Python Conditional Statements Notes
# ==========================================
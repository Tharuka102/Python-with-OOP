# ==========================================
# Python Loops
# Topics:
# 1. for loop
# 2. while loop
# 3. break
# 4. continue
# 5. pass
# ==========================================


# ------------------------------------------
# 1. FOR LOOP
# ------------------------------------------
# Theory:
# A for loop is used to iterate through
# a sequence like list, string, or range.
#
# Syntax:
# for variable in sequence:
#       statements


# Example 1: Print numbers using for loop

for number in range(1, 6):
    print(number)


# Output:
# 1
# 2
# 3
# 4
# 5



# ------------------------------------------
# 2. FOR LOOP WITH LIST
# ------------------------------------------
# A for loop can access each item
# inside a list.


fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)


# Output:
# Apple
# Banana
# Orange



# ------------------------------------------
# 3. FOR LOOP WITH STRING
# ------------------------------------------
# A string is also a sequence.
# The loop accesses each character.


name = "Python"

for letter in name:
    print(letter)



# ------------------------------------------
# 4. WHILE LOOP
# ------------------------------------------
# Theory:
# A while loop executes as long as
# the condition is True.
#
# Syntax:
# while condition:
#       statements


count = 1


while count <= 5:

    print(count)

    # Updating the variable is important
    # to avoid an infinite loop
    count += 1



# ------------------------------------------
# 5. WHILE LOOP WITH USER INPUT
# ------------------------------------------
# The loop continues until the user
# enters 0.


number = 1


while number != 0:

    number = int(input("Enter number (0 to stop): "))

    print("You entered:", number)



# ------------------------------------------
# 6. BREAK STATEMENT
# ------------------------------------------
# Theory:
# break stops the loop immediately.
# The program exits from the loop.


for number in range(1, 10):

    if number == 5:

        # Stop loop when number is 5
        break

    print(number)


# Output:
# 1
# 2
# 3
# 4



# ------------------------------------------
# 7. BREAK WITH WHILE LOOP
# ------------------------------------------


while True:

    user_input = input("Type exit to stop: ")


    if user_input == "exit":

        # Exit the infinite loop
        break


    print(user_input)



# ------------------------------------------
# 8. CONTINUE STATEMENT
# ------------------------------------------
# Theory:
# continue skips the current iteration
# and moves to the next iteration.


for number in range(1, 6):

    if number == 3:

        # Skip number 3
        continue


    print(number)


# Output:
# 1
# 2
# 4
# 5



# ------------------------------------------
# 9. CONTINUE EXAMPLE
# ------------------------------------------
# Print only even numbers


for number in range(1, 10):

    if number % 2 != 0:

        # Skip odd numbers
        continue


    print(number)


# Output:
# 2
# 4
# 6
# 8



# ------------------------------------------
# 10. PASS STATEMENT
# ------------------------------------------
# Theory:
# pass does nothing.
# It is used as a placeholder when
# code block is empty.


for number in range(5):

    if number == 3:

        # Do nothing
        pass


    print(number)



# ------------------------------------------
# 11. PASS IN FUNCTION
# ------------------------------------------
# Empty function using pass


def future_function():

    pass


future_function()



# ------------------------------------------
# 12. NESTED LOOP
# ------------------------------------------
# A loop inside another loop is called
# nested loop.


for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)



# ------------------------------------------
# 13. LOOP WITH ELSE
# ------------------------------------------
# Else block executes after the loop
# finishes normally.


for number in range(5):

    print(number)

else:

    print("Loop Finished")



# ------------------------------------------
# 14. PRACTICAL EXAMPLE
# ------------------------------------------
# Calculate total marks using loop


marks = [80, 75, 90, 85]

total = 0


for mark in marks:

    total = total + mark


print("Total Marks:", total)


# Output:
# Total Marks: 330



# ==========================================
# End of Python Loops Notes
# ==========================================
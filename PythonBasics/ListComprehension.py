# This program takes multiple inputs from user using the List comprehension.
# Displays all the input values on console.

var1, var2 = [int (x) for x in input("Please enter Two numbers\n").split()]
print("First number : ", var1)
print("Second number : ", var2)

"""
when seperating numbers using a comma

var1, var2 = [int(x) for x in input("Please enter Two numbers\n").split(",")]
print("First number : ", var1)
print("Second number : ", var2)
"""

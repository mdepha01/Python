# This programme shows how to declare strings using different quotes

# declaring a string using single quotes
String1 = 'This is a string'

# declaring a string using double quotes
String2 = "This is also a string"

# declaring a string using double quotes
String3 = '''This is another string'''

print("String 1 :", String1)
print("String 2 : ", String2)
print("String 3: ", String3)

# Accessing string characters ---------------------------------

# accessing character in the 3rd character in String 1
print("Third character in String1", String1[2])

# Looping Through strings since they are just arrays -----------
for characters in String1:
    print(characters)

# Reversing a string using [::-1]
RevStr = String3[::-1]
print(RevStr)

# Reversing the string using .join and reversed builtin functions
ReversedString = "".join(reversed(String2))
print(ReversedString)

# accessing a substring
Str = '0123456789'
print(Str[2:7])

# deleting a string character using slicing and concatenation
Str = Str[0:3] + Str[4:]
print(Str)

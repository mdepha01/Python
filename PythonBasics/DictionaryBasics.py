# Dictionary basics

# Creating a Dictionary with mixed keys
Dict1 = {1: 200, 2: 400, 3: {'fruit': 'Banana', 'Veg': 'Spinach'}}
print(Dict1)

# Adding an element in a Dictionary one by one
Dict1[4] = 800
Dict1[5] = 1000
print(Dict1)

# updating an element with a key value 2
Dict1[2] = 'Hello'
print(Dict1)

# Accessing Dictionary elements and printing a value of an element with a key 3
print(Dict1[3])

# Accessing a nested Dictionary using indexing method
print(Dict1[3]['fruit'])
print(Dict1[3]['Veg'])

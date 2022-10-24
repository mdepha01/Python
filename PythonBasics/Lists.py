# Basics of Python List

# Creating a Single Dimension List with different data types and duplicate values

List = [1, 'One', 2, 'Two', 3, 'Three']
print(List)
# Accessing  a single value List using indexing method
Single = List[2]
print(Single)
# Accessing Range of values
SubList = List[1:3]
print(SubList)

# Creating a Multi-Dimensional List
MultiList = [[1, 2, 3], [4, 5, 6]]
print(MultiList)

# Accessing a value 5 in a Multi-Dimensional lise
Val = MultiList[1][1]
print(Val)

# Taking input and store it in a list
String2 = input("Enter comma separated string\n")
InputList = String2.split()
print(InputList)

# Adding an element in a list using append() method
AddList = [1, 2, 3, 4, 5]
print(AddList)
AddList.append(10)
print(AddList)

# adding a list inside another list
List2 = [1, 2, 3, 5]
List3 = [10, 20, 30]
List2.append(List3)
print(List2)

# Adding an element using insert() method
InsertList = [1, 2, 3, 4, 5]
print(InsertList)
InsertList.insert(2, 20)
print(InsertList)

# Object oriented programming basics

# Declaring a class called Person
class Person:
    Name = 'Hello'
    Surname = 'World'
    Age = 2020

    def printDetails(self):
        print(self.Name)
        print(self.Surname)
        print(self.Age)


# Creating an object Student from class Person
Student = Person()
Student.printDetails()  # calling the PrintDetails method


# working with constructors
class Animal:
    def __init__(self, name, classification, colour):  # parametized constructor
        self.name = name
        self.classification = classification
        self.colour = colour

    def details(self):
        print(self.name)
        print(self.classification)
        print(self.colour)

Species = Animal('Lion', 'Carnivore', 'light Brown')
Species.details()

# Inheritance in OOP.Class Son inherits class father attributes
class father:
    def __init__(self,name , surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def Print(self):
        print("Father's name : ", self.name)
        print("Father's  surname: ", self.surname)
        print("Father's Age : ", self.age)

# class son inherits father atrributes
class son(father):
    def Print2(self):
        print("Son's name : ", self.name)
        print("Son's  surname: ", self.surname)
        print("Son's Age : ", self.age)
        print('I inherited those from my dad')

Dad = father('Jon', 'Smith', 35)
Dad.Print()
print()
Kid = son('John', 'Smith jnr', 7)
Kid.Print2()


# Multiple inheritance

#  Parent class
class grandpa:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def Print(self):
        print("Name : ", self.name)
        print("Surname : ", self.surname)
        print("Age : ", self.age)

print()
print()
# Subclass of class grandpa
class pops(grandpa):
    def __init__(self, name, surname, age):
        grandpa.__init__(self, name, surname, age)

    def Display(self):
        print('I inherited this from grandpa')

# subclass of both grandpa and pops
class kiddo(pops):
    def __int__(self, name, surname, age):
        grandpa.__init__(self, name, surname, age)
        pops.__init__(self, name, surname, age)

Oldman = grandpa('John', 'Doe', 78)
Oldman.Print()

papa = pops('Jake', 'Doe', 45)
papa.Print()

elnino = kiddo('Alan', 'Doe', 12)
elnino.Print()

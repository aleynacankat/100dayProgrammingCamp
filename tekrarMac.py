
aleynaName = "Aleyna"
aleynaAge = 22
aleynaGender = "Female"

cankatAge = 34
cankatGender = "Male"

class Person():
    name = ""
    age = 22
    gender = ""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printName(self):
        print(self.name)

aleyna = Person("Aleyna", 22, "Female")


print(aleyna.name)

#myList = list()

#type(myList)

aleyna = Person()

print(type(aleyna))

print(aleyna.age)

type(aleyna)


class Dog():

    year = 7

    def __init__(self, age = 5):
        self.age = age
        self.dogHumanAge = age * self.year
        print("dog instance")

    def humanAge(self):
        return self.age * Dog.year #Dog.year = self.year

myDog = Dog(3)

print(myDog.humanAge())

#Inheritance, Encapsulation, Abstraction, Polymorphism
#oop fundamentals

class Musician():

    def __init__(self):
        print("musician class")

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

aleyna = Musician("Cankat")


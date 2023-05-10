
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

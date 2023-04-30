#Classes

aleynaName = "Aleyna"

aleynaAge = 23

aleynaGender = "Female"

cankatAge = 10

cankatGender = "Gender"

class Person():
    #property
    #name = ""
    #age = 0
    #gender = "" #yazmasan da python bunun name ve age'in olmasini tanımlar
    job = "" #degistirilebilir
    
    #method, initializer
    def __init__(self, nameInput, ageInput, genderInput):
        self.name = nameInput
        self.age = ageInput
        self.gender = genderInput 
        print("init executed") 

    #method
    def test(self):
        print(self.name)

#self sinifin kendisine referans verir. Her zaman sinif tanimlarken self yazilir

#myList = list()

#print(type(myList))

aleyna = Person("Aleyna", 23, "Female")

print(aleyna.name)
print(aleyna.age)
#print(aleyna.printName())

aleyna.job = "Enviromental Engineer"
print(aleyna.job)
#aleyna.name = "Aleyna Cankat Deneme"



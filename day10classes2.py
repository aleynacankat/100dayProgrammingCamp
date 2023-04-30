
class Dog():

    year = 7
    
    def __init__(self, age = 5):
        self.age = age
        self.dogHumanAge = age * self.year
        print("dog instance")

    def humanAge(self):
        return self.age * self.year #Dog.year = self.year

myDog = Dog(3)

print(myDog.age)

print(myDog.humanAge())

print(myDog.dogHumanAge)

barley = Dog()

print(barley)
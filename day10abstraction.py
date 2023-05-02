#Abstraction (soyut sinif)

from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def maxSpeed(self):
        pass
        
#myCar = Car()

class Tesla(Car):
    
    def maxSpeed(self):
        print("200km")

tesla = Tesla()

print(tesla.maxSpeed())

class Mercedes(Car):
    
    def maxSpee(self):
        print("250km")

#mercedes = Mercedes()

#print(mercedes.maxSpeed())

class Fruit():

    def __init__(self,name, calories):
        self.name = name
        self.calories = calories
    def __str__(self):
        return f"{self.name}: {self.calories} calories"

myFruit = Fruit("banana",150)

print(myFruit.calories)

print(myFruit.name)

print(myFruit)

class Train():

    def __init__(self, name):
        self.name = name

    def __getitem__(self,key):
        if key == "a":
            return self.name
        else:
            return "Not found"
    
myTrain = Train("myTrain")

myTrain["a"]

print(myTrain["b"])

#OOPexamples

#oop fundamentals

#abstraction, encapsulation, inheritance, polymorphism

#inheritance = ekstra islerin oldugu 

class Musician():
    def __init__(self, name):
        self.name = name
        print("musician class")
    def test1(self):
        print("test1")
    def test2(self):
        print("test2")

atil = Musician("Aleyna")

class MusicianPlus(Musician):

    def __init__(self,name):
        Musician.__init__(self)
        print("musician plus")

    def test3(self):
        print("test3")

atlas = MusicianPlus()

atlas.name = "Aleyna Cankat"

#polymorphism

class Banana():
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"100 calorie {self.name}"
    
class Apple():
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"150 calorie {self.name}"
    
banana = Banana("banana")

apple = Apple("apple")

print(banana.info())

fruitList = [banana, apple]

for fruit in fruitList:
    print(fruit.info())

#encapsulation: sakli tutmak istedigimiz kod

class Phone():

    def __init__(self,name,price):
        self.name = name 
        self.__prince = price

    def info(self):
        print(f"{self.name} price is {self.__price}")

iphone = Phone("iphone 14", 500)

iphone.info()

#Abstraction: soyut sınıf olusturup kendisini kullanmayip, yapisini kullaniroyruz

from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def maxSpeed():
        pass

myCar = Car()

class Tesla(Car):
    
    def maxSpeed(self):
        print("200km")

tesla = Tesla()

tesla.maxSpeed()

class Mercedes(Car):

    def maxSpee(self):
        print("250 km")

class Fruit():

    def __init__(self,name,calories):
        self.name = name
        self.calories = calories
    
    def __str__(self):
        return f"{self.name}: {self.calories} calories"
    
    def __len__(self):
        return self.calories
    

myFruit = Fruit("banana", 150)

print(myFruit.calories)

print(myFruit.name)

class Train():
    def __init__(self, name):
        self.name = name
    def __getitem__(self,key):
    #if key == "a":
        return self.name
    #else:
        return "Not found"
    
myTrain = Train("myTrain")

myTrain["a"]


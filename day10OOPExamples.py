#inheritance

class Musician():

    def __init__(self, name):
        self.name = name
        print("musician class")

    def test1(self):
        print("test")

    def test2(self):
        print("test2")

aleyna = Musician("Aleyna")

print(aleyna)

print(aleyna.name)

print(aleyna.test1())

print(aleyna.test2())

class MusicianPlus(Musician):
    
    def __init__(self):
        Musician.__init__(self)
        print("musician plus")

    def test3(self):
        print("test3")

    #override
    def test1(self):
        print("test1 test1 test1")
cankat = MusicianPlus("aleynacan")


#Polymorphism

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

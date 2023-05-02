#encapsulation

class Phone():

    def __init__(self, name, price):
        self.name = name   
        self.__price = price #iki alt cizgi ile degistirilemez

    def info(self):
        print(f"{self.name} price is : {self.__price}")

iphone = Phone("iPhone 14", 500)

iphone.price = 400 #bilginin degistirilmesini istemiyorsak

print(iphone.info())


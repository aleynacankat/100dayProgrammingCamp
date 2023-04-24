#If controls

x = 5
y = 2

print(x>y)
print(y<x)

x >= y
print(x>=y)

x = 10
y = 8

print(x == y ) #esit mi degil mi kontrol eder
print(x != y ) #esit mi 

2 > 1 and 3 > 2 # iki kosul da ayni olmali anlamina gelir. İkisinden biri dogru degilse false dondurur

True and True #True

True and False #False

False and False #False

2>1 or 3<2 #True Her iki taraf yanlıssa false doner

#not : olumsuzluk anlamında

not 1 == 1 #False (tersine cevrilir)

List = 10,20,30

print(10 in List) #var mi diye kontrol edilir (True)
print(5 not in List) #var mi diye kontrol edilir (True)

#dictionary de deger kontrolu asagidaki gibi yapilir

my_dictionary = {"a": 10, "b": 20, "c": 30}

print(10 in my_dictionary.values()) #True returnler
print("b" in my_dictionary.keys()) #True returnler

#my_superhero = "Batman"

#print(my_superhero == "Batman")

#if my_superhero == "Batman":
    #indentation
    #print("batmannn")
    #print("aleyna")
my_superhero = input("enter superhero: ")

if my_superhero == "Superman":
    print("Dogru cevap")
elif my_superhero == "Batman":
    print("Yaklastiniz")
elif my_superhero == "Aquaman":
    print("bilemediniz")
else:
    print(":()")

myAge= 19

if myAge <= 18:
    print("age < 18")
elif myAge > 18 and myAge <= 30:
    print("18 - age - 30")
elif myAge > 30 and myAge <=40:
    print("30-40 age")
else:
    print("age >40")


myMarvel = input("enter marvel: ")
marvel =["Spider Man", "Iron Man", "Thor", "Black Widow"]

if myMarvel in marvel:
    print(":)")
else:
    print(":(")

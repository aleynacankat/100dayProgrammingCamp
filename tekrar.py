# for dongusu

sayilar = [1,2,3,6,8,9,5,75,72,15]
isimler = ["aleyna", "cankat", "yagmur"]

for i in sayilar:
    print(i)

for i in sayilar:
    print("Merhaba")


for isim in isimler:
    print(isim)

for a in isim:
    print(a)


_tuple = [(1,2), (4,5), (6,7)]

for a,b in _tuple:
    print(a,b)

_dict = {"k1": 1, "k2": 2, "k3": 3}

for x in _dict:
    print(x)

for x in _dict:
    print(_dict[x])

for x in _dict.values():
    print(x)

for key,value in _dict.items():
    print(key,value)

for c in sayilar:
    if (c % 5 == 0):
        print(c)

# method vs function

myName = "aleyna"

myName.upper()

myNameUpper = myName.upper()

print(myNameUpper)

#functions kod bloklarıdır, duzenler
#girdi alabilir, cikti verebilir

def helloPython():
    print("hello")
    print("python")

print(helloPython())

def helloName(name):
    print("hello")
    print(name)

print(helloName("aleyna"))

def sumexample(num1,num2):
    num3 = num1 + num2
    print(num3)

print(sumexample(20,12))

def helloSurname(surname = "aleyna"):
    print("hello")
    print(surname)

print(helloSurname())

#return

def summation(num1,num2,num3):
    print(num1+num2+num3)

x = summation(10,2,8)

print(type(x))

def Returnsummation(num1, num2, num3):
    return num1 + num2 + num3

#degerini dondurmesi demek 

def controlString(s):
    if s[0] == "a":
        print("a")

print(controlString("aleyna"))



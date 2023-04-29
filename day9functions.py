#method vs function

myName = "Aleyna"

myName.upper()

myNameUpper = myName.upper()

print(myNameUpper)

#help(myNameUpper)

#functions

def hiAleyna(): #define dan gelir
    print("merhaba")
    print("pythonDenemeDef")

print(hiAleyna())

#input

def hiname(name):
    print("hi")
    print(name)
name = "aleyna"

print(hiname(name))

def sumExample(num1, num2):
    print(num1 + num2)

print(sumExample(5,10))

#def sumExample2(num3 + num4):
#    num5 = num3 + num4
#    print(num5)

#print(sumExample2(20,12))

def helloSurname(surname = "cankat"):
    print("hello")
    print(surname)

print(helloSurname())

def summation(num1,num2,num3):
    print(num1+num2+num3)
print(summation(10,2,8))

def returnSummation(num1, num2, num3):
    result = num1 + num2 + num3
#    print(num1 + num2 + num3)
#    return num1+num2+num3
#print(result)

x = returnSummation(10,2,8)
print(x)

def controlString(s):
    if s[0] == "a":
        print("a")

controlString("atlas")

controlString("aleyna")

#args, kwargs (arguments, key word arguments)

def args_sum(*args):
    return sum(args)

print(args_sum(10,20,30,40,50,60))

def argsExample(*args):
    print(args)

argsExample(123,1203123,343,123,34)

def kwargsExample(**kwargs):
    print(kwargs)

kwargsExample(apple=100, banana=150, melon=200)

def kwargsExample2(**kwargs):
    if "apple" in kwargs:
        print("appleeee")
    else:
        print(":()")

kwargsExample2(apple = 10, banana = 15)


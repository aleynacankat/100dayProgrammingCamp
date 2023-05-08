def argsSum(*args):
    return sum(args)

print(argsSum(10,20,30,40,50,60))

def argsExample(*args):
    print(args)

argsExample(123,1325,32) #birden fazla argumanın tutuldugu yer

def kwargsExample(**kwargs):
    print(kwargs)

print(kwargsExample(apple=100, banana=150, melon=200))

def kwargsExample2(**kwargs):
    if "apple" in kwargs:
        print("applee")
    else:
        print(":(")

print(kwargsExample2(apple = 10, banana = 15))

def divideNumber(number):
    return number / 2

print(divideNumber(20))

myList = [3,5,7,10,20,30]

myResultList = []

for num in myList: #map function ile de yapabilirim
    myResultList.append(divideNumber(num))

#map function

print(list(map(divideNumber, myList)))

def controlString(string):
    return "Aleyna" in string

print(controlString("Aleyna Cankat"))

myStringList = ["aleyna", "Aleyna C", "Cankat"]

print(list(map(controlString,myStringList)))

#Filter (sadece istenilen verilere ulasilabilen function)
#map veriyi alir ve farkli bir yer kaydeder

print(list(filter(controlString,myStringList)))

#lambda: 

multiplyLambda = lambda num : num * 3

print(type(multiplyLambda))
print((multiplyLambda(10)))

numList = [10,20,30,40,50]

print(list(map(lambda num:num/4, numList)))


x = 20

def multiply(num):
    x = 5
    return num * 5

print(multiply(10))

print(x)

# LEGB L: Local, E: Enclosing, G: Global, B: Built-in

myStringA = "Aleyna"

def myFunctionA():
    myStringA = "Aleyna 2"

    def myFuction2A():
        myStringA = "Aleyna 3"
        print(myStringA)

y = 10
def newFunction(y):
    print(y)
    y = 5
    print(y)
    return y

print(newFunction(10))


y = 10

def changeY():
    global y
    y = 5
    print(y)
def divideNumber(number):
    return number / 2

print(divideNumber(20))

myList = [3,5,7,10,20,30]

myResultList = []
for num in myList:
    myResultList.append(divideNumber(num))
print(myResultList)

#map #sinif
#help(map)

print(map(divideNumber,myList))

def controlString(string):
    return "Aleyna" in string
print(controlString("AleynaCankat"))

myStringList = ["Aleyna", "Cankat", "Aleyna Cankat"]

print(list(map(controlString, myStringList)))

#Filter

print(list(filter(controlString, myStringList)))

#Lambda

multiplyLambda = lambda num : num * 3
def multiply(num): #lamdanin yaptigiyla ayni sey
    return num * 3 


type(multiplyLambda(10))

result = multiplyLambda(10)

print(result)

numList = [10,20,30,40,50]

print(list(map(lambda num:num/4, numList)))

#Scope

x = 20 

def multiply(num):
    x = 5
    return num * x

print(x)
print(multiply(10))

def multiply(num):
    return num * x
print(multiply(10))

# LEGB -> L : Local, E Enclosing, G Global, B : Built in

#Global
myString = "Aleyna"

def myFunction():
    #Enclosing
    myString = "Aleyna2"
    print(myString)

    def myFunction2():
        #Local
        myString = "Aleyna3"
        print(myString)

    print(myFunction2())

def test1():
    myVariable = 10
    print(myVariable * 3)

def test1():
    print(myVariable * 3)

print(test2())

y = 10
def newFunction(y):
    print(y)
    y = 5
    print(y)
    return y

print(newFunction)


y = 10

def changeY():
    global y    
    y = 5
    print(y)

print(changeY())

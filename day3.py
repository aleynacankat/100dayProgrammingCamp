
#index

myString = "index for day3"

print(myString[4])
print(len(myString)-1)

myName = "james hetfield"
print(myName[(len(myName)-1)])

barcode = "ABCDE123123982"
name = "aleyna"
surname = "cankat"
fullname = name + " " + surname

print(fullname)

print(barcode[0] + barcode[1] + barcode[2]) 

#slicing, starting index, stopping index, stepping size

#print(barcode[#starting index:#stopping index:#stepping index size])
#slicing Veri biliminde çok kullanılır!!

barcode[3::]#DE123123982
barcode[:3:] #ABC
print(barcode[::2]) 
print(barcode[3:5:2]) 
print(barcode[::-1]) #syntaxi ters cevirir
#help(name.index)
name = "samancioglu"
print(name.index("s")) #index kacinci numarada 

print(type(name.split()))


#list metodlari

myString = "list methods"
myString.split()
type(myString.split())
myString = "aleyna"
print(myString[0])

myList = [10, 20, 30]
x = 10
y = 20
z = 30

myList = [x,y,z]
myList = [10,20,30,40,50,60,70]
print(myList[0])
myList[0] = 100
print(myList[0]) #mutable, mutability

print(myList[len(myList)-1]) #-1
print(myList)

myList.append(80)

myList.count(20)

myList.index(40)
print(myList.insert(3,40))
print(myList.pop())
print(myList.remove(40))
print(myList.sort())
print(myList)
#c = input("enter c: ")
#print(c)

#inputList = []
#inputList.append(c)
myString = "python"

#print(inputList)

aleynaList = ["aleyna", "cankat", 23, 3.14]

#nestedList

myNestedList = [10,20,3.14,"aleyna",[1,2,3]]

v = myNestedList[0]
print(v)

smallList = myNestedList[4]

print(smallList[1])
print(myNestedList[4][1])

lastList = ["a","b",["c","d","e"],"f"]

firstList = [10,20,30,40,50,70] #slicing

print(firstList[1:3:2]) #birden başla 3 te dur ve 2 şer atla



myList = [10,20,30,40,50,60,70]

for num in myList:
    print(num /2)

#range(50)

range(0,10)

print(list(range(5,25,2))) #5 ten başla 25 e kadar ikiser arttır demek

myList2 = [10,20,30,40,50,60]

for num in myList2:
    print(num)

for ix in range(len(myList2)): #tum rakamları yazdirdi
    print(myList2[ix])

#enumerate

for element in enumerate(myList2): #tuple olarak vericek
    print(element)

for (ix, value) in enumerate(myList2):
    print(value)

#random

from random import randint

print(randint(0,100))

from random import shuffle

shuffle(myList)

print(myList)

myList3 = [10,20,30,40,50,60,70,80]

print(randint(0,len(myList3)-1))

#zip

foodList = ["apple", "banana","melon"]
caloriesList = [100,150,200]

dayList = ["monday", "tuesday", "wednesday"]

zippedList = list(zip(foodList,caloriesList,dayList))

print(zippedList)

newList = []
myString = "metallica"

for element in myString:
    newList.append(element)
print(newList)

#list comprehension
newList = [element for element in myString] #kisa yolu

print(newList)

numberList = [10,20,30,40,50,60]

newNumberList = [num for num in numberList]
newNumberList = [num for num in numberList]

print(newNumberList)

newNumberList = []
for num in numberList:
    newNumberList.append(num/2)
print(newNumberList)
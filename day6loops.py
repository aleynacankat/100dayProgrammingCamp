#for loop, while loop

#for loop

myList = [10,20,30,40,50,60,70]

for num in myList: #benim listemin içindeki tüm numaralar için
    print(num / 5*2) #her elemanı tek tek yazdirdi

print("for loop started")
for x in myList:
    newNumber = x / 5*2
    print(newNumber)
print("for loop ended")

# myList'te 6 ya tam bolunebilenleri yazdir
for y in myList:
    if y % 6 == 0:
        print(y)

myString = "aleyna cankat"

for c in myString:
    print(c)

myTuple = (10,20,30,40,50,60,70)

for num in myTuple:
    print(num/5*2)

myNewList = [("a", "b"),("c", "d"), ("e", "f"), ("g","h")]

print(len(myNewList))

for element in myNewList:
    print(element)

for (x,y) in myNewList:
    print(x)

mySet = {1,2,3,4,5}
for num in mySet:
    print(num)

myDictionary = {"k1":100, "k2":200, "k3":300}

for element in myDictionary:
    print(element)

for (key, value) in myDictionary.items():
    print(value)

for num in myDictionary.values():
    print(num)

#contiue break  pass (donguden cikmamiza olanak tanir)

myList = [10,20,30,40,50,60,70]

print("for loop started")
for num in myList:
    print(num)
print("for loop ended")

for number in myList:
    print(number)
    if number == 40:
        print("yes")
        break

for number in myList:
    print(number)
    if number == 40:
        print("yes")
        continue

for number in myList:
    if number == 40:
        continue
    print(number) #40 ı atlayıp diger sayilari yazdirdi

for number in myList:
    pass
        
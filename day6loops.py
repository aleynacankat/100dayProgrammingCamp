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
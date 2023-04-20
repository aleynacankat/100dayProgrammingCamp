#dictionary
#key - value pairing

fruitList = ["banana", "apple"]

calorieList = [100, 150]

print(fruitList[0])

fitnessDictionary = {"banana":100, "apple":150}

print(type(fitnessDictionary))

print(fitnessDictionary["banana"]) #sadece anahtarlari yazabiliriz

print(fitnessDictionary.keys())

print(fitnessDictionary.values())

print(list(fitnessDictionary.values())) #dictionarylerde ekleniyor

fitnessDictionary["melon"] = 300
print(fitnessDictionary) #dictionarylerde ekleniyor

print(fitnessDictionary.get("apple",0))

myDictionary = {100:"a", 200:"b", 300:"c"}

print(myDictionary[200]) 

my_mixed_dictionary = {"key1": 100, "key2": 3.14, "key3":[10,20,30]}
print(my_mixed_dictionary["key3"][1])

last_dictionary = {"k1":10, "k2":[10,20,30,40,50], "k3":"string", "k4":{"a":100, "b":200}}

#sets: unique elements, unordered

myList = [10,20,30,40,10,20,40]

mySet = set(myList)
print(mySet)
mySet = {1,23}
mySet2 = {30,40,50,60,70}

print(mySet.union(mySet2))
print(mySet)

countryList = ["de", "fr", "tr", "fr", "de", "tr"]
set(countryList)
print(len(set(countryList))) #verinin iki kez olup tekte kaç tane oldugunun alınmasi

emptyList = []

emptyList.append(10)
emptyList.append(20)
emptyList.append(40)

print(emptyList)

emptySet = {}

print(type(emptySet))

emptySet2 = set()
emptySet2.add(10)
emptySet2.add(10)
emptySet2.add(20)

print(emptySet2)
emptyDictionary = dict()
emptyDictionary["a"] = 10
emptyDictionary["b"] = 20

print(emptyDictionary)

#Tuples



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

    

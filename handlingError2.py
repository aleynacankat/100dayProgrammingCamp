age = input("enter age: ")

print(int(age)*2)

#try - except

while 1==1:
    try:
        myAge = int(input("enter age: "))
        print(myAge * 2)
        break
    except:
        print("enter your age !")
    else:
        print("else executed")
    finally:
        print("finally")


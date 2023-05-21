#%%writefile myfile.text
"""
test 1 
test 2
test 3
"""

myFile = open("myfile.txt")

myFile.seek(0)

myFile.read()

myFile.close()

with open("myfile.txt") as myFile:
    myContent = myFile.read()

with open("myFile.txt", mode = "w") as myNewFile:
    myNewFile.write("test4")

    with open("myFile.txt", mode = "r") as myNewFile:
    myContent = myFile2çread()

#w: wr,te, r: read a: append


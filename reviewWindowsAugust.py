#name = input("What is your name: ")
#print("Welcome again to the analysis" + " " + name)

#Numbers: int / float / complex
num = 100
print(type(num))

num2 = 99.99
print(type(num2))

expression1 = num * 10
print(type(expression1))

expression2 = num + num2
print(type(expression2))

#Math Functions
print(round(2.1))

print(round(5.9))

print(abs(-34))

name = "Python"
name2 = "Pyhton"
name3 = """This is a very long string and supports"""
name4 = 'Hello \"Rockstar Programmer\"'

print(type(name))
print(type(name2))
print(type(name3))
print((name4))

userName = "Aleyna"
age= 23
print(userName + " " +str(age))

first_name = "Aleyna"
last_name = "Cankat"

welcome_message = "Welcome" + " " + first_name + " " + last_name
welcome_message = f"Welcome {first_name} {last_name}"
print(welcome_message)

language = "python"

first_character = language[0]
second_character = language[1]

print(first_character) #p
print(second_character) #y

range1 = language[0:2] # here it starts from index 0 and ends at index 1
range_2 = language[0::1] # starts at 0, stops at end with step over 1
range_3 = language[::2] # starts at 0, till end with step 2
range_4 = language[1:] # starts at index 1 till end of string
range_5 = language[-1] # selects last character
range_6 = language[-2] # second last character
reverse_string = language[::-1] # starts from end and reverses the string
reverse_string_2 = language[::-2] # reverses string and skips 1 character

print(range1) # py
print(range_2) # python
print(range_3) # pto
print(range_4) # ython
print(range_5) # n
print(range_6) # o
print(reverse_string) # nohtyp
print(reverse_string_2) # nhy

favorite_website = 'dev.to'
favorite_website[0] = 'w'
print(favorite_website) # TypeError: 'str' object does not support item assignment

quote = 'javascript is awesome'
print(len(quote)) # 21 (len calculates total no of characters)
new_quote = quote.replace('javascript', 'python')
print(new_quote) # python is awesome
capitalize = new_quote.capitalize()
print(capitalize) # Python is awesome
upper_case = new_quote.upper()
print(upper_case) # PYTHON IS AWESOME

favorite_languages = ['javascript', 'python', 'typescript']
shopping_cart_items = ['pen','toothbrush', 'sanitizer','eraser']
random_things = ['football', 123, True, 'developer', 777]

first_item = shopping_cart_items[0]
print(first_item) # 'pen'

soccer_stars = ['ronaldo', 'messi','ibrahimovic','zidane','beckham']
soccer_stars[0] = 'suarez'
print(soccer_stars) # ['suarez', 'messi','ibrahimovic','zidane','beckham']
range = soccer_stars[0:3]
print(range) # ['suarez', 'messi', 'ibrahimovic']
print(soccer_stars) # ['suarez', 'messi','ibrahimovic','zidane','beckham']
# Note : Slicing lists does not mutate them

clone = soccer_stars[:] # copies the list. Commonly used in Python
print(clone) # ['suarez', 'messi','ibrahimovic','zidane','beckham']
reverse_order = soccer_stars[::-1] # reverses the order of data
print(reverse_order) # ['beckham', 'zidane', 'ibrahimovic', 'messi', 'suarez']

scores = [44,48,55,89,34]
scores.append(100)

print(scores)

scores.insert(0,34)  # Inserts 34 to index 0
scores.insert(2,44) # Inserts 44 to index 2

print(scores) # [34, 44, 44, 48, 55, 89, 34, 100]

scores.extend ([23])  # Extend takes an iterable (loopable items) and adds to end of list
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100, 23]

scores.extend([12,10])
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100, 23, 12, 10]

languages = ['C', 'C#', 'C++']
languages.pop()
print(languages) # ['C', 'C#']
languages.remove('C')
print(languages) # ['C#']
languages.clear()
print(languages) # []

alphabets = ['a', 'b', 'c']
print(alphabets.index('a')) # 0 (Returns the index of the element in list
print(alphabets.count('b')) # 1 (counts the occurence of an element

numbers = [1,4,6,3,2,5]
numbers.sort() # Sorts the list items in place and returns nothing
print(numbers) # [1, 2, 3, 4, 5, 6]

#Python also has a built in sorting function that returns a new list
sorted_numbers = sorted(numbers) # note - this is not a method
print(sorted_numbers) # [1, 2, 3, 4, 5, 6]

numbers.reverse() # reverse the indices in place
print(numbers) # [6, 5, 4, 3, 2, 1]

numbers_clone = numbers.copy() # another approach is numbers[:]
print(numbers_clone) # [6, 5, 4, 3, 2, 1]

avengers = ['ironman', 'spiderman', 'antman', 'hulk']
cloned_avengers = avengers[::1] # very commonly used pattern
reversed_avengers = avengers[::-1] # discussing again because it is also very common
merge_avengers = ' '.join(avengers) # used to join list into string
print(cloned_avengers) # ['ironman', 'spiderman', 'antman', 'hulk']
print(reversed_avengers) # ['hulk', 'antman', 'spiderman', 'ironman']
print(merge_avengers) # ironman spiderman antman hulk

range_of_numbers = list(range(10)) # quickly generates a list of specific range
print(range_of_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
another_range = list(range(0,5)) # with start stop
print(another_range) # [0, 1, 2, 3, 4]

first,second,third = ['tesla','ford','ferarri']
print(first) # tesla
print(second) # second
print(third) # ferarri

a,*others = [1,2,3,4,5] # remaining values are stored in others
print(a) # 1
print(others) # [2, 3, 4, 5]

first,*others,last= [😄,😋,😠,😔,😉]
print(first) # 😄
print(others) # ['😋', '😠', '😔']
print(last) # 😉

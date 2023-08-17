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



"""
for key, value in enumerate(range(10)): # using unpacking techique 
  print(f'key is {key} and value is {value}') # prints key and value at the same time
"""

"""
hungry = True
satisfaction = 0
while(satisfaction < 10):
  satisfaction += 1
  print('Give me something to eat!!') # prints 10 times
"""
"""
hungry = True

satisfaction = 10
while satisfaction < 10:
    satisfaction += 1
    print("give me something to eat")
else:
    print("I'm super satisfied now")
"""
#While vs For Loop

#For loops are usually useful when knowing the range of the iterable that needs to be looped. 
# Whereas while loops can come in handy when we want to perform some task multiple times not knowing the range beforehand.
"""
while True:    
    response_from_user = input("Enter some message. Enter bye to exit")
    if(response_from_user == "bye"):
        break
"""
email_list = ["roger@hey.com", "aleyna@hey.com","roger@hey.com", "prince@gmail.com"]

dublicate_emails = []

for email in email_list:
    if email_list.count(email) > 1 and email not in dublicate_emails:
        dublicate_emails.append(email)
print(dublicate_emails)

def blower(name, emoji):
    print(f"{name} {emoji} {emoji} {emoji}")

blower("fire", "🔥")
blower('water', '🌊')

def multiplier(num1, num2):
  return num1 * num2

result = multiplier(2,3)
print(result) # 6

def sum(num1):
    def child(num2):
        return num1 + num2
    return child

ad_10 = sum(10)
print(ad_10(20))
print(ad_10(50))
print(ad_10(100))

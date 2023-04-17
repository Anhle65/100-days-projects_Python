import random
lenght =input("What lenght of your pefered password: ")
left = int(lenght)
symbols = input("How many symbols you want: ")
left_1 = left - int(symbols)
numbers =input("How many numbers you want: ")
left_2 = left_1 - int(numbers)
specialization = input("How many special characters you want: ")
left_3 = left_2 - int(specialization)
symbol_can_choose = []
for i in range(65, 91):
    char = chr(i)
    symbol_can_choose.append(char)
    lower = chr(i+32)
    symbol_can_choose.append(lower)
number_can_choose =[]
for num in range(10):
    number_can_choose.append(num)
special_character = []
for spe in range(33, 43):
    special_character.append(chr(spe))
password_create = ''
elements = []
if left_3 == 0:
    for i in range(int(symbols)):
        elements.append(random.choice(symbol_can_choose))
    for j in range(int(numbers)):
        elements.append(str(random.choice(number_can_choose)))
    for g in range(int(specialization)):
        elements.append(random.choice(special_character))
    for h in range(int(lenght)):
        concatenate = str(random.choice(elements))
        password_create += concatenate
        elements.remove(concatenate)
    print(f"Your password is: {password_create}")
else:
    print("Your can't create password")

# can use random.shuffer(elements)



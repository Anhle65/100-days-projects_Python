import random
from art_of_hang_man import art
def list_word():
    list_input = input("Enter the list: ")
    chain = list_input.split()
    list(chain)
    rand = random.choice(chain)
    return rand
name = list_word()
list(name)
# print(name)
space = '_' * len(name)
into_list = list(space)
print(space)
i = 0
j = 6

while j > 0 :
    if '_' in into_list:
        guess = input("guess word:")
        for num in range(len(name)):
            if guess == name[num]:
                into_list[num] = guess
        if guess not in into_list:
            j -= 1
            print("You lost one life\n", art[j])
        print (''.join(into_list))
        i += 1
    else:
        break
str = ''
for i in range(len(into_list)):
    in_str = into_list[i]
    str += in_str
if j == 0:
    print("Out of life")
if '_' not in into_list:
    print(f"The answer is {name}. \nYou win")
else:
    print(f"Your answer is {str} \nYou lose")
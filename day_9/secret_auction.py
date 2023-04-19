import os
list_user =[]
user = {}
print("Does anyone want to continue? yes or no")
command = input("Choose the command:\n").lower()
while command == 'yes':
    user['name'] = input("What is your name?\n").capitalize()
    user['bid'] = input("What's your bid?\n$")
    list_user.append(user)
    print("Does anyone want to continue? yes or no")
    command = input("Choose the command:\n").lower()
    os.system('cls')
highest = int(list_user[0]['bid'])
name = list_user[0]['name']
for i in range(len(list_user)):
    if highest < int(list_user[i]['bid']):
        highest = int(list_user[i]['bid'])
        name = list_user[i]['name']
print(f'{name} with the price ${highest} is win')

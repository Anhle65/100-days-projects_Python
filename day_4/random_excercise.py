import random
name_in_list = input("enter the names: ")
names = name_in_list.split()
name_choose = random.randint(0,len(names)-1) #can use randrange(len(names))
print(f"{names[name_choose]} is going to pay")

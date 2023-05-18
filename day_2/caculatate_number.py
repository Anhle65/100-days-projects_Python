number = input("Your number: ")
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print('Total:', sum)
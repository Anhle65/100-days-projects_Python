import random
bid = input("How many you want to bid:\n$")
value = ['11','2','3','4','5','6','7','8','9','10','10','10','10']
player_value = [int(random.choice(value)), int(random.choice(value))]
dealer_value = [int(random.choice(value)), int(random.choice(value))]
print(f'The first value of dealer is {dealer_value[0]}')
condition = True
player_total = sum(player_value)
dealer_total = sum(dealer_value)
end = False
print(f"Your values are {player_value} \nTotal {player_total}")
while condition == True:
    if player_total < 21:
        # end = False
        command = input("Hit or not ?\n").lower()
        if command == 'hit':
            player_value.append(int(random.choice(value)))
            player_total = sum(player_value)
            if 11 in player_value:
                player_total -= 10
        else:
            condition = False
            end == True
        print(f"Your values are {player_value} \nTotal {player_total}")
    else:
        condition = False
        end = True
        if player_total == 21:
            print(f"Blackjack!\nYou win ${bid}")
        else:
            print(f"Your score is {player_total} > 21\nYou lose ${bid}")          
if end == False:
    print(f"Dealer values {dealer_value}")
    print(f'The total value of dealer is {dealer_total}')
    while dealer_total < player_total:
        dealer_value.append(int(random.choice(value)))
        dealer_total = sum(dealer_value)
        print(f"Dealer values {dealer_value}")
        print(f'The total value of dealer is {dealer_total}')
        if 11 in dealer_value:
            dealer_total -= 10
    if dealer_total > 21:
        print(f'You win')
    else:
        if dealer_total == player_total:
            print("Draw")
        else:
            print(f"Dealer win\nTotal {dealer_total}")
    
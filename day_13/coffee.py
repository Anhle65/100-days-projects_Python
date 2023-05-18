from ingredient import *
def name_coffee():
    name = input("""What drink do you want? Espresso/ latte or cappuccino.\nCan choose another command (off/report)""").lower()
    return name
def make_coffee(name):
    for key in MENU[name]['ingredients']:
        if key in resources:
            result = resources[key] - MENU[name]['ingredients'][key]
            resources[key] = result
    return resources
def report(total):
    left = resources
    print(f"Water: {left['water']}ml \nMilk: {left['milk']}ml \nCoffee: {left['coffee']}g\nMoney:{total}")
def if_sufficient(name):
    new_cup = resources
    for key in MENU[name]['ingredients']:
        if new_cup[key] - MENU[name]['ingredients'][key] < 0:
            print (f'Not enough {key}')
            return False
    return True
def coins():
    quarter = int(input('How many quarter coins customer put? '))
    dimes = int(input('How many dimes coins customer put? '))
    nickle = int(input('How many nickle coins customer put? '))
    penny = int(input('How many penny coins customer put? '))
    return quarter*0.25 + dimes*0.1 + nickle*0.05 + penny*0.01
def payment(name, paid):
    cost = MENU[name]['cost']
    if paid < cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    else:
        if paid > cost:
            print(f"Here is ${paid-cost:.2f} dollars in change.")
        return True
def main():
    total = 0
    name = name_coffee()
    resources['Money'] = total
    while name != 'off':
        if name == 'report':
            report(total)
        else:
            if if_sufficient(name) == True:
                print(f"Your coffee cost ${MENU[name]['cost']}")
                paid = coins()
                if payment(name, paid) == True:
                    total += MENU[name]['cost']
                    make_coffee(name)
                    print(f"Enjoy your {name}")
        name = name_coffee()
main()
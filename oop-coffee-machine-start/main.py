import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
oder = input('What drink do you want: (espresso/latte/cappuccino): ').lower()
call_menu = Menu(menu)
make_drink = CoffeeMaker()
payment = MoneyMachine()
print(call_menu)
# cost = MenuItem(call_menu.)
while oder != 'off':
    print(call_menu.get_items())
    call_menu.find_drink(oder)
    make_drink.report()
    payment.report()
    if make_drink.is_resource_sufficient(oder):
        payment.process_coins()
        payment.make_payment(cost)
        make_drink.make_coffee(oder)

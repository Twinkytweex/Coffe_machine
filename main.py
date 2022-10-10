from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



active = True
def coffe_machine():
    money_printer = MoneyMachine()
    menu = Menu()
    coffe_maker = CoffeeMaker()

    while active:
        user = input("Please Type 'y' to start coffe_machine or 'n' to abort:  ").lower()
        if user == 'y':
            user_cho_dri = input(f'please choose the drink ({menu.get_items()}): ').lower()
            user_ver_cho_dri = menu.find_drink(user_cho_dri)
            if coffe_maker.is_resource_sufficient(user_ver_cho_dri) and money_printer.make_payment(user_ver_cho_dri.cost):
                coffe_maker.make_coffee(user_ver_cho_dri)
        elif user == 'report_money':
            money_printer.report()
        elif user == 'report_resources':
            coffe_maker.report()
        else:
            print("Good Bye sir, hope you enjoy our coffe_machine next time ")
            break
        
coffe_machine()       
 
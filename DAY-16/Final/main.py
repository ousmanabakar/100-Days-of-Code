from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



my_coffeemaker=CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
is_on = True


while is_on:
  option = my_menu.get_items()
  choice = input("What would you like? (espresso/latte/cappuccino/):")
  if choice =="off":
    is_on = False

  elif choice == "report":
    my_money_machine.report()
    my_coffeemaker.report()
  else:
    drink = my_menu.find_drink(choice)
    if my_coffeemaker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
      my_coffeemaker.make_coffee(drink)
      


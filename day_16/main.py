from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        command = input(f"What could you like? ({menu.get_items()}):\t").lower()

        match command:
            case "off":
                print("Turning off...")
                return
            case "report":
                coffee_maker.report()
                money_machine.report()
            case _:
                drink = menu.find_drink(command)
                if (drink
                        and coffee_maker.is_resource_sufficient(drink)
                        and money_machine.make_payment(drink.cost)):
                    coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()

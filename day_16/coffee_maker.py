from day_16.menu import MenuItem


class CoffeeMaker:
    """Model the machine that makes coffee."""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Print a report of all resources."""
        print(f"Water: {self.resources['water']}ml\n"
              f"Milk: {self.resources['milk']}ml\n"
              f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """Return True when order can be made, False if ingredients are
        insufficient."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}...")
                return False
        return True

    def make_coffee(self, order: MenuItem):
        """Deduct the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

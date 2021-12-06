"""
Joshua Chen
Assignment 10.1
The purpose of this assignent is to create a custom class that contain data attributes, get method, and also personal created methods
"""

class Fast_Food:
    def __init__(self):
        # Create data attribute for the end result
        self.__recipt = 0
        
    def order(self):
        # Begin class by asking what you want to order

        print("Welcome to Fast Food, please select what you want to order.")
    def end(self, price):
        # Get a price and return your recipt
        self.__recipt = self.__recipt + price
        return f"Your order will come to ${self.__recipt:.2f}"
            
class Burger(Fast_Food):
    def __init__(self, list_of_ingredients):
        # Take in a list of ingredients the derived from the dictionary below it
        self.__list_of_ingredients = list_of_ingredients
        self.__dict_prices_per_ingredients = {"Buns": "0.50", "Patty": "1.00", "Cheese": "0.30", "Bacon": "0.75", "Ketchup": "0.10"}
        # set prices to 0 for an initial data attribute
        self.__prices = 0
        # Inherit recipt for other inheritance
        super().__init__()
    def order(self):
        # Loops each ingredient in the list and converting it into prices
        for x in self.__list_of_ingredients:
            self.__prices = self.__prices + float(self.__dict_prices_per_ingredients[x])
        return(self.__prices)
    def get_ingredients(self):
        # Create an empty list
        list_of_ingredients = []
        # Create a list of ingredient that are avaiable
        for x in self.__dict_prices_per_ingredients:
            list_of_ingredients += [x]
        return list_of_ingredients
    def get_prices_for_ingredients(self):
        # Give you the igredients along with their prices
        return self.__dict_prices_per_ingredients
    def end(self):
        # Returns to the inherited recipt
        return print(super().end(self.order()))

class Drink(Fast_Food):
    def __init__(self, drink, size):
        # A set of private attribute useful for this class
        self.__list_of_drinks = {"Water": "0", "Juice": "0.50", "Soda": "1.00", "Coffee": "1.25", "Iced Tea": "1.00"}
        self.__drink_sizes = {"Large": "0.75", "Medium": "0.50", "Small": "0.25"}
        self.__drink = drink
        self.__size = size
        self.__prices = 0
        super().__init__()
    def order(self):
        # Combine the prices between the type of drink and the size of drink
        self.__prices = self.__prices + float(self.__list_of_drinks[self.__drink]) + float(self.__drink_sizes[self.__size])
        return(self.__prices)
    def get_drinks(self):
        # Create an empty list
        list_of_drinks = []
        list_of_size = []
        # Loops to create a list of drinks
        for x in self.__list_of_drinks:
            list_of_drinks += [x]
        for x in self.__drink_sizes:
            list_of_size += [x]
        return list_of_drinks, list_of_size
    def get_price_for_drinks(self):
        # Return the price from the drinks and the price for the drink size
        return self.__list_of_drinks, self.__drink_sizes
    def end(self):
        # Return the inherited recipt 
        return print(super().end(self.order()))

def main():
    # Start your order
    Fast_Food().order()
    # Choose which ingredients you want
    x = Burger(["Buns", "Patty", "Cheese", "Bacon", "Buns"])
    # If you don't know which ingredients you want, you can see it here
    print(x.get_ingredients())
    # If you want to know the price for the ingredients you want, you can see it here
    print(x.get_prices_for_ingredients())
    x.end()
    # The same similar thing with Burger but applied to drink
    # You choose a drink with the size you want
    y = Drink("Juice", "Large")
    # Get to see the size and type of drink there is
    print(y.get_drinks())
    # Get to see the price of the size and drink
    print(y.get_price_for_drinks())
    y.end()

if __name__ == '__main__':
    main()
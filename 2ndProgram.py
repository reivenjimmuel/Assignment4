
def fruitCost():
    """ Function for each total cost of apples and oranges """
    # The cost of each apple is 20
    apple_ = int(input('Enter the amount of apples that you want to buy: '))*20
    # The cost of each apple is 25
    orange_ = int(input('Enter the amount of oranges that you want to buy: '))*25
    return apple_, orange_

def displayOutput(apple_, orange_):
    print(f'The total amount is Php {apple_+orange_:.2f}.')

apple, orange = fruitCost()
displayOutput(apple, orange)